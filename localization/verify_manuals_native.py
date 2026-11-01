"""Parse source/Chinese pages using the installed GuideME parser, compare AST structure."""
import collections,json,pathlib,subprocess,tempfile
import manual_translation as m
from source_archive import guideme_classpath
def count_nodes(node):
 c=collections.Counter()
 def visit(v):
  if isinstance(v,dict):
   if v.get('type') in ['mdxJsxTextElement','mdxJsxFlowElement'] and v.get('name')=='a' and any(a.get('name')=='name' for a in v.get('attributes',[])):
    return # Generated, independently validated named anchors.
   if 'type' in v and v['type'] not in ['text','yamlFrontmatter']:c[v['type']]+=1
   for key,value in v.items():
    if key!='position':visit(value)
  elif isinstance(v,list):
   for value in v:visit(value)
 visit(node);return c
with tempfile.TemporaryDirectory(prefix='manual-parser-') as tmp:
 tmp=pathlib.Path(tmp);source=tmp/'source';ast=tmp/'ast'
 for key,text in m.sources().items():
  p=source/key;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
 cp=guideme_classpath()
 args=['java',f'-DastOutput={ast}','--class-path',':'.join(cp),str(m.ROOT/'localization/ValidateManuals.java'),str(source),str(m.PACK)]
 result=subprocess.run(args,text=True,capture_output=True)
 (m.BASE/'native-parser-check.txt').write_text(result.stdout+result.stderr)
 assert result.returncode==0,result.stderr
 diffs=[]
 for key in m.sources():
  a=json.loads((ast/str(source/key).lstrip('/')).with_suffix('.md.json').read_text())
  b=json.loads((ast/str(m.target(key)).lstrip('/')).with_suffix('.md.json').read_text())
  c,d=count_nodes(a),count_nodes(b)
  if c!=d:diffs.append({'page':key,'added':dict(d-c),'removed':dict(c-d)})
 (m.BASE/'ast-structure-review.json').write_text(json.dumps(diffs,ensure_ascii=False,indent=2)+'\n')
 print(result.stdout.strip())
 print('AST differences:',json.dumps(diffs,ensure_ascii=False))
 assert not diffs,'Review/fix AST structural differences before completion'
