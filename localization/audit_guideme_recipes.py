"""Audit every effective GuideME recipe component against current static inputs.

This inventory resolves FTB Materials outputs, data-pack overrides, never
conditions and the explicit removal list. Dynamic KubeJS and client loading
remain runtime acceptance; findings are never hidden with empty fallbackText.
"""
import collections,json,pathlib,re,sys,zipfile
from feedback_fixes import ROOT,GAME,BASE,sha,encode
from source_archive import libraries_directory
import release_pack
TAG=re.compile(r'<(RecipeFor|RecipesFor|Recipe)\b[^>]*\bid="([^"]+)"[^>]*>')

def visible_source(text):
    """Mask Markdown comment definitions and fenced examples, retaining lines."""
    lines=[];fence=None
    for line in text.splitlines(keepends=True):
        stripped=line.lstrip()
        marker=re.match(r'(`{3,}|~{3,})',stripped)
        hidden=fence is not None or bool(marker) or stripped.startswith('[//]:')
        if marker:
            if fence is None:fence=marker[1][0]
            elif marker[1][0]==fence:fence=None
        lines.append(('\n' if line.endswith('\n') else '') if hidden else line)
    return ''.join(lines)

def main():
    recipes={};pages={};sources={};dynamic=[];unparsed=[]
    def read_member(member,data,origin):
        if member.startswith('data/') and '/recipe/' in member and member.endswith('.json'):
            ns,rel=member[5:].split('/recipe/',1)
            try:recipes[ns+':'+rel[:-5]]=(json.loads(data),origin)
            except (ValueError,UnicodeDecodeError) as error:unparsed.append({'member':member,'origin':origin,'error':str(error)})
        elif member.startswith('assets/') and member.endswith(('.md','.mdx')) and '/oracle_index/' not in member:
            # Other locales cannot affect the Simplified Chinese effective page.
            if re.search(r'/_([a-z]{2}_[a-z]{2})/',member) and '/_zh_cn/' not in member:return
            pages[member]=(data.decode(),origin)
    # Only the patched client of the instance's NeoForge build; launchers keep several side by side.
    neoforge=json.loads((GAME/'instance.json').read_text())['modLoader'].removeprefix('neoforge-')
    jars=list(libraries_directory().glob(f'net/neoforged/minecraft-client-patched/{neoforge}/*.jar'))+sorted((GAME/'mods').glob('*.jar'))
    for jar in jars:
        sources[str(jar)]=sha(jar.read_bytes())
        with zipfile.ZipFile(jar) as z:
            for member in z.namelist():
                if member.endswith(('.json','.md','.mdx')) and (member.startswith('data/') and '/recipe/' in member or member.startswith('assets/') and member.endswith(('.md','.mdx'))):
                    read_member(member,z.read(member),str(jar))
    # Actual pack overrides. These are read directly from target_instance.
    for pack in sorted((GAME/'datapacks').iterdir()):
        if pack.is_dir():
            for p in pack.glob('data/*/recipe/**/*.json'):
                sources[str(p)]=sha(p.read_bytes());read_member(p.relative_to(pack).as_posix(),p.read_bytes(),str(p))
        elif pack.suffix=='.zip':
            sources[str(pack)]=sha(pack.read_bytes())
            with zipfile.ZipFile(pack) as z:
                for member in z.namelist():
                    if member.startswith('data/') and '/recipe/' in member and member.endswith('.json'):read_member(member,z.read(member),str(pack))
    for p in (GAME/'kubejs/assets').rglob('*'):
        if p.is_file() and p.suffix in ['.md','.mdx']:
            sources[str(p)]=sha(p.read_bytes());read_member('assets/'+p.relative_to(GAME/'kubejs/assets').as_posix(),p.read_bytes(),str(p))
    outputs,_,_=release_pack.assemble_resourcepack([])
    for member,(data,origin) in outputs.items():read_member(member,data,origin)
    # Prefer a translated document over its corresponding base-language page.
    effective={}
    for member,(text,origin) in pages.items():
        canonical=member.replace('/_zh_cn/','/')
        if canonical not in effective or '/_zh_cn/' in member:effective[canonical]=(member,text,origin)
    db=json.loads((GAME/'config/ftbmaterials/unifier-db.json').read_text());mapping=db['items'];tagmap=db['item_tags']
    removals=GAME/'kubejs/server_scripts/recipes/removals.js';source=removals.read_text()
    removed=set(re.findall(r'"([a-z0-9_]+:[^"\n]+)"',source.split('const removeRecipeId = [',1)[1].split('];',1)[0]))
    for p in (GAME/'kubejs/server_scripts').rglob('*.js'):
        text=p.read_text()
        if 'ServerEvents.recipes' in text:sources[str(p)]=sha(p.read_bytes())
        if '.remove(' in text and 'ServerEvents.recipes' in text and p!=removals:dynamic.append(str(p.relative_to(GAME)))
    def item_values(v):
        if isinstance(v,str):
            if v.startswith('#'):return [tagmap[v[1:]]] if v[1:] in tagmap else []
            return [mapping.get(v,v)] if re.fullmatch(r'[\w.-]+:[\w/.-]+',v) else []
        if isinstance(v,list):return [x for t in v for x in item_values(t)]
        if isinstance(v,dict):
            # Result schemas differ; only descend through output containers.
            return [x for k,t in v.items() if k in {'id','item','tag','stack','result','output','results','outputs'} for x in item_values(('#'+t) if k=='tag' and isinstance(t,str) else t)]
        return []
    by_output=collections.defaultdict(list);enabled={};conditions={}
    for rid,(data,origin) in recipes.items():
        cond=data.get('neoforge:conditions',[])
        if rid in removed or any(c.get('type')=='neoforge:never' for c in cond):continue
        enabled[rid]=(data,origin)
        if cond:conditions[rid]=cond
        for k in ['result','results','output','outputs','secondary','secondary_output']:
            for item in item_values(data.get(k)):by_output[item].append(rid)
    rows=[]
    for canonical,(member,text,origin) in sorted(effective.items()):
        text=visible_source(text)
        for m in TAG.finditer(text):
            ns=member.split('/')[1];rid=m[2] if ':' in m[2] else ns+':'+m[2]
            if m[1]=='Recipe':candidates=[rid] if rid in enabled else []
            else:candidates=by_output.get(rid,[])
            note=re.search(r'fallbackText="([^"]+)"',m[0])
            row={'page':member,'line':text[:m.start()].count('\n')+1,'tag':m[1],'id':rid,'candidates':sorted(candidates),'recipe_types':sorted({enabled[k][0].get('type','unknown') for k in candidates}),'status':'static_candidate_found' if candidates else 'requires_review','visible_fallback':note[1] if note else None}
            documented=[c for c in json.loads((BASE/'component-corrections.json').read_text()) if c['page']==member and 'id="'+rid+'"' in c['new']]
            if not candidates and documented:
                row['status']='documented_no_recipe'
                row['classification']=documented[0]['classification']
            rows.append(row)
    report={'target_pack_version':json.loads((ROOT/'project.json').read_text())['target_pack_version'],'effective_documents':len(effective),'documents_with_recipe_components':len({r['page'] for r in rows}),'components':len(rows),'static_candidates':sum(bool(r['candidates']) for r in rows),'documented_no_recipe':sum(r['status']=='documented_no_recipe' for r in rows),'requires_review':[r for r in rows if r['status']=='requires_review'],'dynamic_recipe_scripts_not_executed':dynamic,'unifier_database_sha256':sha((GAME/'config/ftbmaterials/unifier-db.json').read_bytes()),'limitations':['Candidate recipes are not proof of client-side rendering. Mod conditions, tags, dynamic KubeJS mutations, and recipe synchronization require runtime verification.','Datapack ordering follows static pack inventory; runtime enabled packs were not interrogated.'],'in_game_tested':False,'references':rows}
    (BASE/'guideme-recipe-audit.json').write_bytes(encode(report))
    (BASE/'guideme-recipe-audit-inputs.json').write_bytes(encode({'sha256':sources,'unparsed_recipe_resources':unparsed}))
    assert not unparsed,unparsed[:3]
    print(json.dumps({k:v for k,v in report.items() if k not in ['references','requires_review']},ensure_ascii=False,indent=2));print('Needs review:',len(report['requires_review']))
    for r in report['requires_review']:print(r['page'],r['line'],r['tag'],r['id'])
if __name__=='__main__':main()
