import pathlib,json,zipfile,subprocess,collections,hashlib,shutil,sys
BASE=pathlib.Path(__file__).resolve().parent;ROOT=BASE.parents[2]
sys.path.insert(0,str(ROOT/'localization'));from source_archive import guideme_classpath,mods_directory,read_resource
d=json.loads((ROOT/'localization/cfpa_review/decisions/manuals.json').read_text())
source=BASE/'validation/source';target=BASE/'validation/chinese';ast=(BASE/'validation/ast').absolute()
for generated in (source,target,ast):
 if generated.exists():shutil.rmtree(generated)
validated_hashes={}
for row in d:
 if row['format']!='Markdown/MDX' or row['status']!='accepted':continue
 # The recorded JAR path is provenance; resolve the page from the current instance,
 # preferring the same JAR file when several mods ship the same page (AE2 / ae2wtlib).
 raw=read_resource(row['path'],mods_directory()/pathlib.Path(row['source']['target_source']).name)[0].decode()
 validated_hashes[row['path']]={'source_lf':hashlib.sha256(raw.replace('\r\n','\n').replace('\r','\n').encode()).hexdigest(),'chinese':hashlib.sha256((ROOT/row['file']).read_bytes()).hexdigest()}
 for root,text in [(source,raw),(target,(ROOT/row['file']).read_text())]:
  path=root/row['path'];path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
cp=guideme_classpath()
r=subprocess.run(['java',f'-DastOutput={ast}','--class-path',':'.join(cp),str(ROOT/'localization/ValidateManuals.java'),str(source),str(target)],text=True,capture_output=True)
(BASE/'native-parser-check.txt').write_text(r.stdout+r.stderr);print(r.stdout,r.stderr);assert r.returncode==0

def counts(node):
 c=collections.Counter()
 def visit(v):
  if isinstance(v,dict):
   if v.get('name')=='a' and any(a.get('name')=='name' for a in v.get('attributes',[])):return
   if 'type' in v and v['type'] not in ['text','yamlFrontmatter']:c[v['type']]+=1
   for key,value in v.items():
    if key!='position':visit(value)
  elif isinstance(v,list):
   for value in v:visit(value)
 visit(node);return c
# Text emphasis may split across Chinese phrases, and CFPA groups the same terminal
# slot descriptions into a list. These reviewed presentation differences retain all prose.
REVIEWED={
 'assets/ae2/ae2guide/example-setups/processor-automation.md':({'missing':{},'extra':{'strong':1}},'源句 WILL NOT MATCH WHAT YOU SEE IN JEI 在中文拆为两个强调片段, 语义完整'),
 'assets/ae2/ae2guide/example-setups/storage-types.md':({'missing':{},'extra':{'strong':1}},'CFPA 对不会主动迁移增加强调, 正文含义与当前英文一致'),
 'assets/ae2/ae2guide/items-blocks-machines/terminals.md':({'missing':{},'extra':{'list':1,'listItem':4,'strong':1}},'样板编码槽位的4段内容组织为列表, 仍含4种类型子列表; ASAP 译为尽快并强调'),
}
def table_shape(n):
 out=[]
 def walk(v):
  if isinstance(v,dict):
   if v.get('type')=='table':out.append([len(r.get('children',[])) for r in v.get('children',[])])
   for key,value in v.items():
    if key!='position':walk(value)
  elif isinstance(v,list):
   for value in v:walk(value)
 walk(n);return out
out=[];reviewed=[];table_pages=0
for row in d:
 if row['format']!='Markdown/MDX' or row['status']!='accepted':continue
 a=json.loads((ast/(str(source/row['path']).lstrip('/')+'.json')).read_text());b=json.loads((ast/(str(target/row['path']).lstrip('/')+'.json')).read_text());ac,bc=counts(a),counts(b)
 assert table_shape(a)==table_shape(b),('table_shape',row['path'])
 if table_shape(a):table_pages+=1
 if ac!=bc:
  delta={'missing':dict(ac-bc),'extra':dict(bc-ac)}
  entry={'path':row['path'],**delta}
  if row['path'] in REVIEWED and delta==REVIEWED[row['path']][0]:
   reviewed.append({**entry,'reason':REVIEWED[row['path']][1]})
  else:out.append(entry)
(BASE/'ast-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))

(BASE/'ast-reviewed-differences.json').write_text(json.dumps(reviewed,ensure_ascii=False,indent=2)+'\n')
print('AST reviewed presentation differences:',len(reviewed),'table pages:',table_pages,'unresolved:',len(out))
assert not out, 'Unreviewed AST differences remain'
def metadata_without_display(value,path=()):
 if isinstance(value,dict):return {key:metadata_without_display(v,path+(key,)) for key,v in value.items() if not(key in {'title','description','tooltip'} and path in {(),('navigation',)})}
 if isinstance(value,list):return [metadata_without_display(v,path) for v in value]
 return value
metadata_differences=[]
for row in d:
 if row['format']!='Markdown/MDX' or row['status']!='accepted':continue
 def metadata(root):return json.loads((ast/(str(root/row['path']).lstrip('/')+'.json.yaml.json')).read_text())
 if metadata_without_display(metadata(source))!=metadata_without_display(metadata(target)):metadata_differences.append(row['path'])
(BASE/'yaml-metadata-review.json').write_text(json.dumps(metadata_differences,ensure_ascii=False,indent=2)+'\n')
assert not metadata_differences,'Non-display navigation/icon/category/item metadata changed'
(BASE/'native-input-hashes.json').write_text(json.dumps(validated_hashes,ensure_ascii=False,indent=2)+'\n')
