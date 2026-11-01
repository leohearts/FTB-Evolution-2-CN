"""Validate feedback Markdown and YAML using this instance's native GuideME."""
import json,subprocess
from feedback_fixes import BASE,OUTPUT,ROOT
from source_archive import guideme_classpath
cp=guideme_classpath()
result=subprocess.run(['java','--class-path',':'.join(cp),str(ROOT/'localization/ValidateManuals.java'),str(OUTPUT)],text=True,capture_output=True)
(BASE/'native-parser-check.txt').write_text(result.stdout+result.stderr)
print(result.stdout)
assert result.returncode==0,result.stderr
expected=len(list(OUTPUT.rglob('*.md')))
assert f'parsed {expected} pages successfully' in result.stdout,expected
