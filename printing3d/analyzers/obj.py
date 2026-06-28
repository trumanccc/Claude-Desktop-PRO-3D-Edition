from pathlib import Path
def analyze(path):
 txt=Path(path).read_text(errors='ignore').splitlines()
 return {'vertices':sum(1 for l in txt if l.startswith('v ')),
'faces':sum(1 for l in txt if l.startswith('f '))}
