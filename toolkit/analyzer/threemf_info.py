from zipfile import ZipFile
from pathlib import Path
import sys

if len(sys.argv)!=2:
    raise SystemExit("Usage: python threemf_info.py model.3mf")
zf=ZipFile(sys.argv[1])
print({"entries":len(zf.namelist()),"has_model":any(n.endswith(".model") for n in zf.namelist())})
