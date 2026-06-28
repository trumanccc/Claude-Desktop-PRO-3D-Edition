import json
from pathlib import Path
def save(data,outfile):
    Path(outfile).write_text(json.dumps(data,indent=2),encoding="utf8")
