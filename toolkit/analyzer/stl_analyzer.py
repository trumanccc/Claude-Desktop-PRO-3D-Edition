from pathlib import Path
import sys
if len(sys.argv)!=2:
    print("Usage: python stl_analyzer.py file.stl")
    raise SystemExit(1)
p=Path(sys.argv[1])
print("File:",p.name)
print("Size:",p.stat().st_size,"bytes")
