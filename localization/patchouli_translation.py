"""Generic Patchouli book translation: extract/build/check with zh_cn overlays."""
from protected_text import signature
import collections, hashlib, json, pathlib, re, sys, zipfile
from punctuation import assert_ascii, normalize, normalize

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / 'localization/patchouli'
PACK = ROOT / '.minecraft/resourcepacks/FTB-Evolution-2-Manuals-zh_CN'
INSTALLED = ROOT.parent / 'FTB-Evolution-2-CN'  # unused placeholder
ZIP_MAIN = pathlib.Path('/home/astronw/.ftba/instances/ftb evolution 2/resourcepacks/FTB-Evolution-2-1.4.0-zh_CN.zip')

# namespace -> (book, source, base) ; base: None | 'jar' | 'installed'
BOOKS = {
    'mffs': [('handbook', ('jar', 'mffs-5.8.39.jar'), None)],
    'animal_pen': [('guide_book', ('jar', 'animal_pen-neoforge-26.1-2.5.2.jar'), None)],
    'apotheosis': [('apoth_chronicle', ('jar', 'Apotheosis-26.1.2-9.1.0.jar'), 'jar')],
    'arsmagicalegacy': [('arcane_compendium', ('jar', 'arsmagicalegacy-26.1.2-1.7.1.jar'), None)],
    'modularrouters': [('book', ('jar', 'modular-routers-26.1.2.2.jar'), 'installed')],
    'productivebees': [('guide', ('jar', 'productivebees-26.1.2-15.4.0.jar'), 'installed')],
    'justdirethings': [('justdirethingsbook', ('kubejs', None), 'jar')],
    'iceandfire': [('iceandfire', ('jar', 'iceandfire-2.2-beta.4.jar'), None)],
}

TEXT_KEYS = {'name', 'title', 'text', 'description', 'headline', 'subtitle', 'landing_text', 'tooltip'}
LANG_REF = re.compile(r'^[a-z0-9_]+(\.[a-z0-9_]+)+$')
CJK = re.compile(r'[\u3400-\u9fff]')

_installed_cache = {}
def installed_zh(ns, book, rel):
    key = (ns, book, rel)
    if key not in _installed_cache:
        member = f'assets/{ns}/patchouli_books/{book}/zh_cn/{rel}'
        try:
            with zipfile.ZipFile(ZIP_MAIN) as z:
                _installed_cache[key] = json.loads(z.read(member)) if member in z.namelist() else None
        except Exception:
            _installed_cache[key] = None
    return _installed_cache[key]

def jar_zh(ns, book, rel, source):
    if source[0] != 'jar':
        return None
    member = f'assets/{ns}/patchouli_books/{book}/zh_cn/{rel}'
    try:
        with zipfile.ZipFile(ROOT / '.minecraft/mods' / source[1]) as z:
            return json.loads(z.read(member)) if member in z.namelist() else None
    except Exception:
        return None

def base_json(ns, book, rel, source, base):
    if base == 'jar':
        return jar_zh(ns, book, rel, source)
    if base == 'installed':
        return installed_zh(ns, book, rel)
    return None

def book_files(ns, book, source):
    kind, jar = source
    if kind == 'jar':
        with zipfile.ZipFile(ROOT / '.minecraft/mods' / jar) as z:
            prefix = f'assets/{ns}/patchouli_books/{book}/en_us/'
            for n in sorted(z.namelist()):
                if n.startswith(prefix) and n.endswith('.json'):
                    overlay = ROOT / '.minecraft/kubejs' / n
                    text = overlay.read_text() if overlay.is_file() else z.read(n).decode()
                    yield n.removeprefix(prefix), text, None
    else:
        folder = ROOT / f'.minecraft/kubejs/assets/{ns}/patchouli_books/{book}/en_us'
        for p in sorted(folder.rglob('*.json')):
            yield p.relative_to(folder).as_posix(), p.read_text(), None

def walk(node, path):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, f'{path}/{k}')
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f'{path}/{i}')
    elif isinstance(node, str):
        yield path, node

def book_lang(ns, source):
    kind, jar = source
    try:
        if kind == 'jar':
            with zipfile.ZipFile(ROOT / '.minecraft/mods' / jar) as z:
                path = f'assets/{ns}/lang/en_us.json'
                if path in z.namelist():
                    return set(json.loads(z.read(path)))
        else:
            return set(json.loads((ROOT / f'.minecraft/kubejs/assets/{ns}/lang/en_us.json').read_text()))
    except Exception:
        return set()
    return set()

def segments(text, lang_keys=frozenset()):
    data = json.loads(text)
    for path, value in walk(data, ''):
        key = path.rsplit('/', 1)[-1]
        if key in TEXT_KEYS and re.search('[A-Za-z]', value) and value.strip():
            if LANG_REF.match(value) and (not re.search(r'\s', value)) and value in lang_keys:
                continue
            yield path, value

def protections(value):
    return {
        'syntax': signature(value),
        'macros': sorted(re.findall(r'\$\([^)]{1,120}?\)', value)),
        'percent': value.count('%%'),
        'numbers': sorted(re.findall(r'(?<![\w#])\d+(?:[,.]\d+)*(?:%%)?', value)),
        'newlines': value.count('\n'),
    }

def set_path(node, path, value):
    parts = [p for p in path.split('/') if p]
    for part in parts[:-1]:
        node = node[int(part)] if part.isdigit() else node[part]
    last = parts[-1]
    if last.isdigit():
        node[int(last)] = value
    else:
        node[last] = value

def build_one(cmd, ns, book, source, base):
    out_root = PACK / f'assets/{ns}/patchouli_books/{book}/zh_cn'
    lang_keys = book_lang(ns, source)
    report = []
    for rel, text, _ in book_files(ns, book, source):
        seg = dict(segments(text, lang_keys))
        trans_path = BASE / 'translations' / ns / book / (rel + '.tsv')
        data = {}
        if trans_path.exists():
            for line in trans_path.read_text().splitlines():
                if not line:
                    continue
                p, v = line.split('\t', 1)
                data[p] = v.replace('\\n', '\n')
        unknown = set(data) - set(seg)
        assert not unknown, (ns, book, rel, 'unknown segment', sorted(unknown)[:4])
        bj = base_json(ns, book, rel, source, base)
        complete = set(seg) <= set(data) or bj is not None
        if not complete:
            report.append({'ns': ns, 'book': book, 'file': rel, 'segments': len(seg),
                           'translated': len([p for p in seg if p in data]), 'complete': False})
            continue
        if not seg:
            report.append({'ns': ns, 'book': book, 'file': rel, 'segments': 0, 'translated': 0, 'complete': True})
            continue
        data_out = json.loads(text)
        if isinstance(bj, dict):
            # adopt upstream/CFPA Chinese where the en structure has the same slot
            for path, value in walk(bj, ''):
                if path not in seg:
                    continue  # Keep current effective IDs/components and non-display fields.
                if CJK.search(value):
                    value = normalize(value)
                try:
                    node = data_out
                    parts = [p for p in path.split('/') if p]
                    ok = True
                    for part in parts[:-1]:
                        if part.isdigit():
                            part = int(part)
                            if isinstance(node, list) and part < len(node):
                                node = node[part]
                            else:
                                ok = False; break
                        elif isinstance(node, dict) and part in node:
                            node = node[part]
                        else:
                            ok = False; break
                    last = parts[-1]
                    if ok:
                        if last.isdigit():
                            last = int(last)
                            if isinstance(node, list) and last < len(node):
                                node[last] = value
                        elif isinstance(node, dict):
                            node[last] = value
                except Exception:
                    pass
        for path, value in seg.items():
            if path not in data:
                continue
            zh = data[path]
            exp, act = protections(value), protections(zh)
            assert exp == act, (ns, book, rel, path, 'protected', exp, act, value, zh)
            if not (zh == value and CJK.search(value)):
                assert_ascii(zh, (ns, book, rel, path))
            set_path(data_out, path, zh)
        out = json.dumps(data_out, ensure_ascii=False, indent=2) + '\n'
        target = out_root / rel
        if cmd == 'build':
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(out)
        else:
            assert target.read_text() == out, (ns, book, rel, 'output drift')
        report.append({'ns': ns, 'book': book, 'file': rel, 'segments': len(seg),
                       'translated': len([p for p in seg if p in data]), 'complete': True})
    return report

def cmd_extract(sel):
    BASE.mkdir(parents=True, exist_ok=True)
    manifest = {}
    report = []
    for ns, book, source, base in sel:
        lang_keys = book_lang(ns, source)
        for rel, text, _ in book_files(ns, book, source):
            manifest[f'{ns}/{book}/{rel}'] = hashlib.sha256(text.encode()).hexdigest()
            bj = base_json(ns, book, rel, source, base)
            bj_data = json.loads(json.dumps(bj)) if bj is not None else None
            seg = []
            for path, value in segments(text, lang_keys):
                if bj_data is not None:
                    try:
                        node = bj_data
                        parts = [p for p in path.split('/') if p]
                        ok = True
                        for part in parts:
                            if part.isdigit():
                                part = int(part)
                                if isinstance(node, list) and part < len(node):
                                    node = node[part]
                                else:
                                    ok = False; break
                            elif isinstance(node, dict) and part in node:
                                node = node[part]
                            else:
                                ok = False; break
                        if ok and isinstance(node, str) and CJK.search(node):
                            continue
                    except Exception:
                        pass
                seg.append((path, value))
            tpath = BASE / 'translations' / ns / book / (rel + '.tsv')
            if not seg or tpath.exists():
                continue
            tpath.parent.mkdir(parents=True, exist_ok=True)
            lines = [f'{path}\t' + value.replace('\n', '\\n') for path, value in seg]
            tpath.write_text('\n'.join(lines) + '\n')
            report.append((ns, book, rel, len(seg)))
    mf = BASE / 'source_manifest.json'
    old = json.loads(mf.read_text()) if mf.exists() else {}
    mf.write_text(json.dumps({**old, **manifest}, indent=1, sort_keys=True) + '\n')
    for ns, book, rel, n in report:
        print(ns, book, rel, n, 'segments')

def cmd_check(sel):
    allr = []
    for ns, book, source, base in sel:
        allr += build_one('check', ns, book, source, base)
    (BASE / 'progress.json').write_text(json.dumps(allr, indent=1) + '\n')
    print(sum(r['segments'] for r in allr), 'segments,',
          sum(r['translated'] for r in allr), 'translated,',
          sum(1 for r in allr if r['segments'] and r['complete']), 'files complete')

def cmd_build(sel):
    allr = []
    for ns, book, source, base in sel:
        allr += build_one('build', ns, book, source, base)
    (BASE / 'progress.json').write_text(json.dumps(allr, indent=1) + '\n')
    print(sum(r['translated'] for r in allr), 'translated fields,',
          sum(1 for r in allr if r['segments'] and r['complete']), 'files written')

def main():
    cmd = sys.argv[1]
    want = set(sys.argv[2:]) or set(BOOKS)
    sel = [(ns, book, source, base) for ns, books in BOOKS.items() if ns in want for book, source, base in books]
    if cmd == 'extract':
        cmd_extract(sel)
    elif cmd == 'check':
        cmd_check(sel)
    elif cmd == 'build':
        cmd_build(sel)
    else:
        raise SystemExit('unknown command')
if __name__ == '__main__':
    main()
