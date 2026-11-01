"""Independent checks for the remaining 1.4.0 manual batch.

Runs the project-wide token checks, then compiles every translated GuideME/MDX
page with the GuideME native parser and compares AST node counts, table shapes
and non-display frontmatter.  Stellaris uses its own Stellardown syntax and is
covered by the token checks only.
"""
from __future__ import annotations

import collections
import json
import pathlib
import re
import shutil
import subprocess
import sys

from source_archive import guideme_classpath

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / 'localization/manuals_extra'
MANIFEST = BASE / 'source_manifest.json'
SOURCES = BASE / 'sources'
TRANSLATIONS = BASE / 'translations'
TEMP = BASE / '.verify'
PACK = ROOT / '.minecraft/resourcepacks/FTB-Evolution-2-Manuals-zh_CN'
DATAPACK = ROOT / '.minecraft/datapacks/ftb_evolution_cn'


def counts(node):
    counter = collections.Counter()

    def visit(value):
        if isinstance(value, dict):
            if value.get('name') == 'a' and any(attr.get('name') == 'name' for attr in value.get('attributes', [])):
                return
            if 'type' in value and value['type'] not in {'text', 'yamlFrontmatter'}:
                counter[value['type']] += 1
            for key, child in value.items():
                if key != 'position':
                    visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(node)
    return counter


def table_shape(node):
    shapes = []

    def visit(value):
        if isinstance(value, dict):
            if value.get('type') == 'table':
                shapes.append([len(row.get('children', [])) for row in value.get('children', [])])
            for key, child in value.items():
                if key != 'position':
                    visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(node)
    return shapes


def metadata_without_display(value, path=()):
    if isinstance(value, dict):
        return {
            key: metadata_without_display(child, path + (key,))
            for key, child in value.items()
            if not (key in {'title', 'description', 'tooltip'} and path in {(), ('navigation',)})
        }
    if isinstance(value, list):
        return [metadata_without_display(child, path) for child in value]
    return value


def output_for(target: str) -> pathlib.Path:
    if target.startswith('datapacks/'):
        return DATAPACK / target.removeprefix('datapacks/ftb_evolution_cn/')
    return PACK / target


# Source hard wraps can create a bare ``10.``/``30.`` line that Markdown parses
# as a spurious ordered list.  The Chinese translation joins the number back
# into the sentence, which is the intended rendering.  Keep these exact deltas
# reviewed instead of reproducing an accidental list in the game.
REVIEWED_AST = {
    'assets/oracle_index/books/kindredspirits/docs/kindred_charm.mdx': (
        {'list': 1, 'listItem': 1},
        '源文硬换行留下孤立的 10. 行, 原生解析器把它当成有序列表; 中文将数字并回句子.',
    ),
    'assets/oracle_index/books/kindredspirits/docs/spirits/trex.mdx': (
        {'paragraph': 1, 'list': 1, 'listItem': 1},
        '源文硬换行把 30. 留在列表项缩进内, 原生解析器把它当成嵌套列表; 中文将数字并回句子.',
    ),
}


def run_native(pages: dict[str, dict]) -> tuple[int, list[dict]]:
    if TEMP.exists():
        shutil.rmtree(TEMP)
    (TEMP / 'source').mkdir(parents=True)
    (TEMP / 'chinese').mkdir(parents=True)
    native = {path: entry for path, entry in pages.items() if entry['format'] == 'md' or entry['format'] == 'mdx'}
    native = {path: entry for path, entry in native.items() if not path.startswith('data/stellaris/')}
    for path in native:
        for root, origin in (('source', SOURCES), ('chinese', TRANSLATIONS)):
            destination = TEMP / root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(origin / path, destination)
    classpath = ':'.join(guideme_classpath())
    temp_rel = TEMP.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ['java', f'-DastOutput={temp_rel}/ast', '--class-path', classpath,
         str(ROOT / 'localization/ValidateManualsExtra.java'),
         f'{temp_rel}/source', f'{temp_rel}/chinese'],
        cwd=ROOT, text=True, capture_output=True,
    )
    if result.returncode != 0:
        return result.returncode, [{'error': 'native parser failed', 'stdout': result.stdout, 'stderr': result.stderr}]
    problems = []
    reviewed_ast = []
    for path in native:
        base = TEMP / 'ast' / temp_rel / 'source' / path
        chinese = TEMP / 'ast' / temp_rel / 'chinese' / path
        source_json = pathlib.Path(str(base) + '.json')
        chinese_json = pathlib.Path(str(chinese) + '.json')
        source_yaml = pathlib.Path(str(base) + '.json.yaml.json')
        chinese_yaml = pathlib.Path(str(chinese) + '.json.yaml.json')
        if not (source_json.is_file() and chinese_json.is_file()):
            problems.append({'page': path, 'error': 'missing AST output'})
            continue
        left = json.loads(source_json.read_text())
        right = json.loads(chinese_json.read_text())
        left_counts = counts(left)
        right_counts = counts(right)
        if left_counts != right_counts:
            missing = dict(left_counts - right_counts)
            extra = dict(right_counts - left_counts)
            reviewed = REVIEWED_AST.get(path)
            if reviewed and not extra and missing == reviewed[0]:
                reviewed_ast.append({'page': path, 'missing': missing, 'reason': reviewed[1]})
            else:
                problems.append({
                    'page': path,
                    'error': 'AST node counts differ',
                    'missing': missing,
                    'extra': extra,
                })
        if table_shape(left) != table_shape(right):
            problems.append({'page': path, 'error': 'table shape differs'})
        if source_yaml.is_file() and chinese_yaml.is_file():
            left_meta = metadata_without_display(json.loads(source_yaml.read_text()))
            right_meta = metadata_without_display(json.loads(chinese_yaml.read_text()))
            if left_meta != right_meta:
                problems.append({'page': path, 'error': 'non-display frontmatter differs', 'source': left_meta, 'chinese': right_meta})
    return 0, problems, reviewed_ast


def main() -> None:
    token = subprocess.run(
        [sys.executable, 'localization/manual_extra_translation.py', 'check'],
        cwd=ROOT, text=True, capture_output=True,
    )
    if token.returncode != 0:
        print(token.stdout + token.stderr)
        raise SystemExit('token checks failed')
    manifest = json.loads(MANIFEST.read_text())
    translated = {
        path: entry for path, entry in manifest['documents'].items()
        if (TRANSLATIONS / path).is_file()
    }
    stellar_problems = []
    for path in translated:
        if not path.startswith('data/stellaris/'):
            continue
        text = (TRANSLATIONS / path).read_text()
        openings = len(re.findall(r'\[ref=[^\]]+\]', text))
        closings = len(re.findall(r'\[ref\]', text))
        if openings != closings:
            stellar_problems.append({'page': path, 'error': 'unbalanced [ref] markers', 'open': openings, 'close': closings})
        for marker in ('[item=', '[entity=', '[block=', '[image='):
            if text.count(marker) != (TRANSLATIONS / path).read_text().count(marker):
                pass
    missing_outputs = []
    for path, entry in translated.items():
        output = output_for(entry['target'])
        if not output.is_file() or output.read_text().replace('\r\n', '\n') != (TRANSLATIONS / path).read_text().replace('\r\n', '\n'):
            missing_outputs.append(str(output.relative_to(ROOT)))
    native_code, native_problems, reviewed_ast = run_native(translated)
    report = {
        'status': 'passed' if native_code == 0 and not native_problems and not missing_outputs and not stellar_problems else 'failed',
        'pages_in_scope': len(manifest['documents']),
        'pages_translated': len(translated),
        'pages_native_checked': len([path for path in translated if not path.startswith('data/stellaris/')]),
        'pages_token_checked': len(translated),
        'outputs_missing_or_drifted': missing_outputs,
        'native_problems': native_problems,
        'reviewed_ast_differences': reviewed_ast,
        'stellar_problems': stellar_problems,
        'in_game_tested': False,
    }
    (BASE / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'native_problems'}, ensure_ascii=False, indent=2))
    if report['status'] != 'passed':
        print(json.dumps(native_problems[:20], ensure_ascii=False, indent=2))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
