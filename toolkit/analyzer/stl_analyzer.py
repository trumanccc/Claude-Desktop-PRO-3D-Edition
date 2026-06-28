from pathlib import Path
import struct,sys

def analyze(path):
    p=Path(path)
    with p.open('rb') as f:
        header=f.read(80)
        ascii_mode=header.lower().startswith(b'solid')
        f.seek(80)
        data=f.read(4)
    tris=struct.unpack('<I',data)[0] if (not ascii_mode and len(data)==4) else None
    return {
        "file":p.name,
        "size_bytes":p.stat().st_size,
        "format":"ASCII STL" if ascii_mode else "Binary STL",
        "triangles":tris
    }

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python stl_analyzer.py model.stl")
    print(analyze(sys.argv[1]))
