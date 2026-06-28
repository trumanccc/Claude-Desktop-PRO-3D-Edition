from pathlib import Path
import sys
txt=Path(sys.argv[1]).read_text(errors='ignore').splitlines()
v=sum(1 for l in txt if l.startswith('v '))
f=sum(1 for l in txt if l.startswith('f '))
print({'vertices':v,'faces':f})
