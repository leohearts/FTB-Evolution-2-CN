"""Reviewed 1.5.1 -> 1.6.3 localization migration; writes the worktree only.

Run one step at a time from the project root, e.g.
  python -c "import sys;sys.path.insert(0,'localization/updates/1.6.3');import migrate;migrate.quests()"
Steps with a ``prepare`` flag only write the pending review lists.
"""
from pathlib import Path
import difflib, hashlib, json, re, shutil, sys
ROOT=Path(__file__).resolve().parents[3];BASE=Path(__file__).parent;VERSION='1.6.3'
sys.path.insert(0,str(ROOT/'localization'))
CONFIG=json.loads((ROOT/'project.json').read_text());GAME=Path(CONFIG['target_instance']);W=ROOT/CONFIG['worktree']
def read(p):return json.loads(Path(p).read_text())
def sha(raw):return hashlib.sha256(raw).hexdigest()
def backup(p):
 p=Path(p).absolute();out=BASE/'before'/p.relative_to(ROOT)
 if p.is_file() and not out.exists():out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,out)
 return out
def write(p,data):
 p=Path(p).absolute();backup(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data.encode() if isinstance(data,str) else data)
def dump(p,data):write(p,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def unchanged_pairs(old,new):
 """Index pairs of lines/segments whose English text is unchanged."""
 return [(b.a+i,b.b+i) for b in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_matching_blocks() for i in range(b.size)]
def aligned(old,new,oldzh):
 return {b:oldzh[a] for a,b in unchanged_pairs(old,new) if a in oldzh}

def quests():
 import quest_translation as q
 overrides=read(BASE/'quest-translations.json');terms=read(q.WORK/'terms.json');records=[];old_to_new={}
 for p in sorted(q.SOURCE.rglob('*.json5')):
  rel=p.relative_to(q.SOURCE)
  oldpath=backup(p);old=q.segments(q.load_source(oldpath));newpath=GAME/p.relative_to(W);new=q.segments(q.load_source(newpath))
  target=q.WORK/'translations'/rel.with_suffix('.json');oldzh=read(backup(target))
  pairs=[(str(a),str(b)) for a,b in unchanged_pairs(old,new) if str(a) in oldzh]
  out={b:oldzh[a] for a,b in pairs};indices=dict(pairs)
  for i,text in enumerate(new):
   if text in overrides:out[str(i)]=overrides[text];records.append({'file':str(rel),'segment':i,'source':text,'translation':overrides[text]})
   elif str(i) not in out and text not in terms:
    prior={oldzh[str(j)] for j,s in enumerate(old) if s==text and str(j) in oldzh}
    if len(prior)!=1:raise ValueError((str(rel),i,text))
    out[str(i)]=prior.pop()
  q.translate(q.load_source(newpath),out,terms)
  # Keep the reviewed file byte-for-byte when its English segments did not change.
  if old!=new or out!=oldzh:dump(target,out)
  write(p,newpath.read_bytes());old_to_new[str(target.relative_to(ROOT))]=indices
 for p in (GAME/'config/ftbquests/quests').rglob('*'):
  if p.is_file() and 'lang' not in p.relative_to(GAME/'config/ftbquests/quests').parts:write(W/p.relative_to(GAME),p.read_bytes())
 dump(q.WORK/'source_manifest.json',{str(p.relative_to(q.SOURCE)):sha(p.read_bytes()) for p in sorted(q.SOURCE.rglob('*.json5'))})
 from source_archive import read_resource
 names=read(q.WORK/'quest_item_names.json');jar=next((GAME/'mods').glob('ftb-evolution-companion-*.jar'));names['source_jar']=str(Path('.minecraft/mods')/jar.name)
 raw,evidence=read_resource(names['language_file'],jar);live=json.loads(raw)
 # New companion keys do not affect these names; every bound English value must still match.
 assert all(live.get(k)==e['en'] for k,e in names['entries'].items()),'Quest-name source changed'
 names['resource_binding']=evidence;dump(q.WORK/'quest_item_names.json',names)
 extra=read(q.WORK/'quest_extra_labels.json')
 for group in extra:
  if group['source'].endswith('ftb-en_us.json'):
   source=GAME/'kubejs/assets/ftb/lang/en_us.json';write(ROOT/group['source'],source.read_bytes());group['source_sha256']=sha(source.read_bytes())
 dump(q.WORK/'quest_extra_labels.json',extra)
 path=q.WORK/'feedback_20261019/quest-name-changes.json';changes=read(backup(path))
 for row in changes:
  if row['file'] not in old_to_new:continue
  if row['key'] in old_to_new[row['file']]:row['key']=old_to_new[row['file']][row['key']]
  else:
   # The segment was re-reviewed: follow it to the reviewed text that still carries the approved name.
   found=[r['segment'] for r in records if 'localization/translations/'+str(Path(r['file']).with_suffix('.json'))==row['file'] and row['en'] in r['source'] and row['zh'] in r['translation']]
   assert len(found)==1,row;row['key']=str(found[0])
 dump(path,changes);dump(BASE/'quest-deltas.json',records)

def custom():
 bindings=read(ROOT/CONFIG['custom_adaptation']['source_bindings']);bindings['target_pack_version']=VERSION
 for ns,row in bindings['sources'].items():
  data=(GAME/row['path']).read_bytes();write(W/row['path'],data);row['sha256']=sha(data)
 dump(ROOT/f'localization/custom/source-bindings-{VERSION}.json',bindings)
 # Typo fix in the pack source (Jewler -> Jeweler); the reused Chinese name is unchanged.
 path=ROOT/'localization/custom/batches/batch-001/manifest.json';manifest=read(backup(path))
 en=read(GAME/'kubejs/assets/ftb/lang/en_us.json')
 for row in manifest['reused_language']:
  if row['key']=='ftb.shopkeeper.jewler':assert row['en']=='The Jewler';row['en']=en[row['key']]
 dump(path,manifest)
 tsv=ROOT/'localization/custom/pack.tsv';text=backup(tsv).read_text();assert 'The Jewler\t珠宝商\n' in text
 write(tsv,text.replace('The Jewler\t珠宝商\n','The Jeweler\t珠宝商\n'))

# JEI 29.47 also nests mezz_config 0.6.6; JarJar loads the newest copy, the 0.6.9 standalone one.
NESTED_REBIND={'batch-327':['META-INF/jarjar/mezz_config-26.1.2-neoforge-0.6.9.jar']}

def ordinary():
 import ordinary_translation as o
 from source_archive import read_resource
 records=[];revisions=read(o.WORK/'overlay-revisions.json');reviewed=read(BASE/'language-translations.json')
 for folder in sorted(o.WORK.glob('batch-*')):
  if not (folder/'verification.json').exists():continue
  # Batches added for this version are already bound to the current sources.
  if read(folder/'manifest.json').get('target_pack_version')==VERSION and 'resource_binding' in read(folder/'manifest.json') and not (BASE/'before'/folder.relative_to(ROOT)).exists():continue
  oldmanifest=read(backup(folder/'manifest.json'));old=read(backup(folder/'source-en_us.json'));values=read(backup(folder/'source-values.json'));zh={}
  for line in backup(folder/'zh-values.tsv').read_text().splitlines():
   i,v=line.split('\t',1);zh[values[int(i)]]=v.replace('\\n','\n')
  oldzh={k:oldmanifest['context_overrides'].get(k,zh[v]) for k,v in old.items()};manifest=dict(oldmanifest)
  container=manifest.pop('source_container',None)
  preferred=ROOT/(container['jar'] if container else manifest['jar'])
  nested=[container['member']] if container else [x['path'] for x in manifest.get('nested_jars',[])] if 'nested_jars' in manifest else [manifest['nested_jar']] if 'nested_jar' in manifest else []
  nested=NESTED_REBIND.get(folder.name,nested)
  mod_id=next(iter(oldmanifest.get('resource_binding',{}).get('mod_ids',[])),None)
  raw,evidence=read_resource(manifest['language_path'],preferred,mod_id=mod_id,nested_paths=nested)
  jar=Path(evidence['jar']);manifest['jar']=str(Path('.minecraft/mods')/jar.name);manifest['jar_sha256']=evidence['jar_sha256'];manifest['resource_binding']=evidence
  for k in ['nested_jar','nested_jar_sha256','nested_jars']:manifest.pop(k,None)
  if evidence['nested_jars']:manifest['nested_jars']=evidence['nested_jars']
  current=json.loads(raw);selected={k:v for k,v in current.items() if k in old};changes={k:{'old':old[k],'new':v} for k,v in selected.items() if old[k]!=v}
  for k,r in changes.items():
   assert k in reviewed,(folder.name,k,r);newzh=reviewed[k]['translation'];assert reviewed[k]['source']==r['new'],k
   revision={'batch':folder.name,'namespace':manifest['namespace'],'key':k,'source':r['new'],'previous':oldzh[k],'translation':newzh,'reason':reviewed[k]['reason']}
   if revision not in revisions:revisions.append(revision)
   oldzh[k]=newzh
  manifest['include_keys']=list(selected);newvals=list(dict.fromkeys(selected.values()));seen={}
  for k,en in selected.items():seen.setdefault(en,oldzh[k])
  manifest['context_overrides']={k:oldzh[k] for k,en in selected.items() if k in oldmanifest['context_overrides'] or oldzh[k]!=seen[en]}
  manifest['unchanged_values']=[v for v in oldmanifest.get('unchanged_values',[]) if v in newvals]+[v for v in newvals if v not in oldmanifest.get('unchanged_values',[]) and not re.search('[\u3400-\u9fff]',seen[v])]
  dump(folder/'manifest.json',manifest);dump(folder/'source-en_us.json',selected);dump(folder/'source-values.json',newvals)
  write(folder/'zh-values.tsv','\n'.join(str(i)+'\t'+seen[v].replace('\n','\\n') for i,v in enumerate(newvals))+'\n')
  records.append({'batch':folder.name,'state':'active','namespace':manifest['namespace'],'old_jar':oldmanifest['jar'],'jar':manifest['jar'],'jar_sha256':manifest['jar_sha256'],'language_path':manifest['language_path'],'language_sha256':sha(raw),'source_changes':changes,'removed_compatibility_keys':{k:{'source':v,'translation':oldzh[k]} for k,v in old.items() if k not in current},'before':str((BASE/'before'/folder.relative_to(ROOT)).relative_to(ROOT))})
 dump(o.WORK/'overlay-revisions.json',revisions);dump(BASE/'ordinary-rebind.json',{'target_pack_version':VERSION,'batches':records,'in_game_tested':False})
 for folder in sorted(o.WORK.glob('batch-*')):
  if (folder/'verification.json').exists():o.process(folder,True)

def cfpa():
 """Adapt reviewed CFPA decisions whose current English changed; retire removed keys."""
 review=read(BASE/'cfpa-review-adaptation.json');folder=ROOT/'localization/cfpa_review/decisions'
 for name in sorted({r['file'] for r in [*review['adapted'].values(),*review['retired'].values()]}):
  decisions=read(backup(folder/name))
  for d in decisions:
   if d['key'] in review['adapted'] and review['adapted'][d['key']]['file']==name:
    r=review['adapted'][d['key']];assert d['status']=='accepted' and d['english']==r['previous_english'] and d['chinese']==r['previous_chinese'],d['key']
    d.setdefault('changes',[]).append({'from':d['chinese'],'to':r['chinese'],'reason':f"{VERSION}: {r['reason']}"})
    d['english']=r['english'];d['chinese']=r['chinese']
   elif d['key'] in review['retired'] and review['retired'][d['key']]['file']==name:
    r=review['retired'][d['key']];assert d['english']==r['english'],d['key']
    d['status']='rejected';d['reason']=r['reason']
  dump(folder/name,decisions)

def core_manuals(prepare=False):
 import manual_translation as m
 mf=m.BASE/'source_manifest.json';prior=read(backup(mf));pending={};records=[]
 # Pack English overrides of the core guides take precedence over the JAR copies.
 for ns,root in [('ftb','guides/ftb'),('ftbic','ftbic'),('nodeworks','nodeworksguide')]:
  for p in (GAME/f'kubejs/assets/{ns}/{root}').rglob('*.md'):write(W/p.relative_to(GAME),p.read_bytes())
 current=m.sources();reviewed=read(BASE/'core-manual-translations.json') if (BASE/'core-manual-translations.json').exists() else {}
 assert set(prior)<=set(current),'A core page disappeared; review its migration first'
 for key,text in current.items():
  if sha(text.encode())==prior.get(key):continue
  trans=m.BASE/'translations'/Path(key).with_suffix('.json');oldzh=read(backup(trans)) if trans.exists() else {}
  snapshot=m.BASE/'sources'/key;old=backup(snapshot).read_text() if snapshot.exists() else ''
  if old:assert sha(old.encode())==prior[key],(key,'historical source mismatch')
  out={str(k):v for k,v in aligned(old.splitlines(),text.splitlines(),{int(k):v for k,v in oldzh.items()}).items()}
  for i,line in m.segments(text):
   if str(i) in out:continue
   match=reviewed.get(key,{}).get(str(i))
   if match:assert match['source']==line,(key,i);out[str(i)]=match['translation']
   else:pending.setdefault(key,{})[str(i)]={'source':line}
  if not prepare and key not in pending:dump(trans,out);write(snapshot,text)
  records.append({'page':key,'old_sha256':prior.get(key),'source_sha256':sha(text.encode()),'reviewed_segments':len(reviewed.get(key,{})),'pending_segments':len([i for i,_ in m.segments(text) if str(i) not in out]),'translated_lines':len(out)})
 dump(BASE/'core-manual-pending.json',pending)
 if prepare:return
 assert not pending,'Review core-manual-pending.json'
 dump(mf,{k:sha(v.encode()) for k,v in current.items()});dump(BASE/'core-manual-deltas.json',records)

NEW_EXTRA_PAGES=['assets/nautec/guides/nautec/guide/laser_chemistry/crystal_cultivator.md',
 'assets/rep_ae2_bridge/guides/rep_ae2_bridge/guide/index.md','assets/rep_ae2_bridge/guides/rep_ae2_bridge/guide/bridge.md',
 'assets/rep_ae2_bridge/guides/rep_ae2_bridge/guide/matter_assembler.md','assets/rep_ae2_bridge/guides/rep_ae2_bridge/guide/matter_storage.md']

def extra_manuals(prepare=False):
 import manual_extra_translation as m
 from source_archive import read_resource
 prior=read(backup(m.MANIFEST));manifest=json.loads(json.dumps(prior));records=[];pending={}
 reviewed=read(BASE/'extra-manual-translations.json') if (BASE/'extra-manual-translations.json').exists() else {}
 def resolve(path,source):
  live=GAME/'kubejs'/path
  if live.exists():return m.normalize(live.read_text()),str(live),None
  if Path(source).suffix=='.jar':
   raw,evidence=read_resource(path,source);return m.normalize(raw.decode('utf-8-sig')),evidence['jar'],evidence
  return m.normalize(Path(source).read_text()),source,None
 def translate(path,old,oldzh,text):
  a,b=old.splitlines(),text.splitlines();zh=oldzh.splitlines();assert len(a)==len(zh),path
  out=aligned(a,b,dict(enumerate(zh)))
  for i,line in enumerate(b):
   if i in out:continue
   match=reviewed.get(path,{}).get(str(i))
   if match:assert match['source']==line,(path,i);out[i]=match['translation']
   elif not line.strip() or not re.search('[A-Za-z]',line):out[i]=line
   else:pending.setdefault(path,{})[str(i)]={'source':line}
  if not prepare and path not in pending:write(m.TRANSLATIONS/path,'\n'.join(out[i] for i in range(len(b)))+'\n')
 for path,entry in manifest['documents'].items():
  source=m.SOURCES/path;oldsource=backup(source).read_text();oldzh=backup(m.TRANSLATIONS/path).read_text();assert m.digest(oldsource)==entry['source_sha256']
  text,origin,evidence=resolve(path,entry['source'])
  if m.digest(text)!=entry['source_sha256']:
   translate(path,oldsource,oldzh,text);records.append({'page':path,'old_sha256':entry['source_sha256'],'new_sha256':m.digest(text)})
  if not prepare:
   entry['source']=origin;entry['source_sha256']=m.digest(text);entry['english_words_approx']=m.word_count(text)
   if evidence:entry['resource_binding']=evidence
   write(source,text)
 jar={r['path']:r['source'] for r in read(ROOT/f'localization/reports/update-{VERSION}-assessment.json')['manual_new_page_candidates']}
 roots=m.guide_roots({p:{} for p in [*manifest['documents'],*NEW_EXTRA_PAGES]})
 for path in NEW_EXTRA_PAGES:
  assert path not in manifest['documents'],path
  text,origin,evidence=resolve(path,str(jar[path]))
  translate(path,'','',text);records.append({'page':path,'old_sha256':None,'new_sha256':m.digest(text)})
  if not prepare:
   entry={'path':path,'source':origin,'format':'md','group':path.split('/')[1],'target':m.target_for(path,roots),'english_words_approx':m.word_count(text),'source_sha256':m.digest(text)}
   if evidence:entry['resource_binding']=evidence
   manifest['documents'][path]=entry;write(m.SOURCES/path,text)
 dump(BASE/'extra-manual-pending.json',pending)
 if prepare:return
 assert not pending,'Review extra-manual-pending.json'
 manifest['documents']=dict(sorted(manifest['documents'].items()))
 manifest['target_pack_version']=VERSION;manifest['known_pages']=sorted(m.known_pages());dump(m.MANIFEST,manifest);dump(BASE/'extra-manual-deltas.json',records)
