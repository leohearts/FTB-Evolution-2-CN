"""Resolve current archive resources without treating versioned filenames as identity.

Only resource bytes (or explicit class bytes) are accepted against a reviewed
hash. This never rewrites a manifest or accepts changed source content.
"""
from functools import lru_cache
import hashlib
import io
import json
import tomllib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def mods_directory():
    config = json.loads((ROOT / 'project.json').read_text())
    return Path(config['target_instance']) / 'mods'


def libraries_directory():
    """Launcher library root: `minecraft_libraries` in project.json, else the FTB App layout."""
    config = json.loads((ROOT / 'project.json').read_text())
    return Path(config.get('minecraft_libraries') or Path(config['target_instance']).parents[1] / 'bin/libraries')


def guideme_classpath():
    """The instance's GuideME plus the parser dependencies it expects from the launcher."""
    libraries = libraries_directory()
    return [str(next(mods_directory().glob('guideme-*.jar')))] + [
        str(next(libraries.rglob(name))) for name in ['gson-2.13.2.jar', 'slf4j-api-2.0.17.jar', 'guava-33.5.0-jre.jar']]



def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def mod_ids(jar):
    with zipfile.ZipFile(jar) as archive:
        if 'META-INF/neoforge.mods.toml' in archive.namelist():
            return [m['modId'] for m in tomllib.loads(archive.read('META-INF/neoforge.mods.toml').decode())['mods']]
        if 'fabric.mod.json' in archive.namelist():
            return [json.loads(archive.read('fabric.mod.json'))['id']]
    return []


@lru_cache(maxsize=8)
def _index(folder, stamp):
    """Resource names only; no global language-key precedence is guessed."""
    index = {}
    def visit(archive, jar, chain):
        for name in archive.namelist():
            if name.endswith('.jar') and name.startswith(('META-INF/jarjar/', 'META-INF/jars/')):
                embedded = archive.read(name)
                with zipfile.ZipFile(io.BytesIO(embedded)) as nested:
                    visit(nested, jar, chain + ((name, digest(embedded)),))
            else:
                index.setdefault(name, []).append((jar, chain))
    for jar in sorted(Path(folder).glob('*.jar')):
        with zipfile.ZipFile(jar) as archive:
            visit(archive, jar, ())
    return index


def read_resource(member, preferred=None, expected_sha256=None, mods=None, mod_id=None, nested_paths=None):
    """Return bytes and actual provenance; missing/ambiguous/changed is an error."""
    folder = Path(mods) if mods is not None else mods_directory()
    preferred = Path(preferred) if preferred is not None else None
    if (mod_id is None and preferred is not None and preferred.is_file()
            and preferred.parent.resolve() == folder.resolve()):
        identities = mod_ids(preferred)
        if identities:
            mod_id = identities[0]
    if mod_id is not None:
        # Never let an old preferred filename hide two installed versions of
        # the same mod. Metadata indexing is cheap and cached in this process.
        provider = find_mod(mod_id, folder)
        preferred = provider
    if (preferred is not None and preferred.is_file()
            and preferred.parent.resolve() == folder.resolve()
            and mod_id is not None):
        # An already bound current provider needs no scan of hundreds of other
        # archives. Inspect its nested containers so their provenance is retained.
        local_index = {}
        def visit(archive, chain):
            for name in archive.namelist():
                if name == member:
                    local_index.setdefault(name, []).append((preferred, chain))
                elif name.endswith('.jar') and name.startswith(('META-INF/jarjar/', 'META-INF/jars/')):
                    embedded = archive.read(name)
                    with zipfile.ZipFile(io.BytesIO(embedded)) as nested:
                        visit(nested, chain + ((name, digest(embedded)),))
        with zipfile.ZipFile(preferred) as archive:
            visit(archive, ())
        matches = local_index.get(member, [])
    else:
        paths = sorted(folder.glob('*.jar'))
        stamp = tuple((p.name, p.stat().st_mtime_ns, p.stat().st_size) for p in paths)
        matches = _index(str(folder), stamp).get(member, [])
    if mod_id is not None:
        matches = [(p, chain) for p, chain in matches if mod_id in mod_ids(p)]
    # A preferred archive can be an explicitly extracted non-top-level source.
    preferred = Path(preferred) if preferred is not None else None
    if mod_id is not None and preferred is not None and preferred.is_file():
        explicit = [(p, chain) for p, chain in matches if p.resolve() == preferred.resolve()]
        if explicit:
            matches = explicit
    if nested_paths is not None:
        explicit_chain = [(p, chain) for p, chain in matches if [n for n, _ in chain] == nested_paths]
        if explicit_chain:
            matches = explicit_chain
    # One mod can ship a direct language file and a nested integration overlay.
    # An explicit direct provider is unambiguous within that same archive.
    if len(matches) > 1 and len({str(p) for p, _ in matches}) == 1:
        direct = [(p, chain) for p, chain in matches if not chain]
        if len(direct) == 1:
            matches = direct
    if len(matches) != 1:
        raise ValueError(f'{member}: expected one current provider, found {len(matches)}: '
                         + ', '.join(str(p) for p, _ in matches))
    jar, chain = matches[0]
    raw = jar.read_bytes()
    provenance = {'jar': str(jar), 'jar_sha256': digest(raw),
                  'nested_jars': [{'path': n, 'sha256': h} for n, h in chain],
                  'resource': member, 'mod_ids': mod_ids(jar)}
    for name, _ in chain:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            raw = archive.read(name)
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        raw = archive.read(member)
    provenance['resource_sha256'] = digest(raw)
    if expected_sha256 is not None and digest(raw) != expected_sha256:
        raise ValueError(f'{member}: source content changed; review the English/class delta '
                         f'before rebinding ({expected_sha256} -> {digest(raw)})')
    return raw, provenance

@lru_cache(maxsize=8)
def _mod_index(folder, stamp):
    result = {}
    for name, _, _ in stamp:
        jar = Path(folder) / name
        for mod_id in mod_ids(jar):
            result.setdefault(mod_id, []).append(jar)
    return result


def find_mod(mod_id, mods=None):
    folder = Path(mods) if mods is not None else mods_directory()
    stamp = tuple((p.name, p.stat().st_mtime_ns, p.stat().st_size)
                  for p in sorted(folder.glob('*.jar')))
    matches = _mod_index(str(folder), stamp).get(mod_id, [])
    if len(matches) != 1:
        raise ValueError(f'{mod_id}: expected one current mod, found {len(matches)}')
    return matches[0]
