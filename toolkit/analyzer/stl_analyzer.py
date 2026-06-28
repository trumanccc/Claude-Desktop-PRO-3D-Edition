from pathlib import Path
import struct,sys
if len(sys.argv)!=2:
    print('Usage: python stl_analyzer.py model.stl'); raise SystemExit(1)
p=Path(sys.argv[1])
with p.open('rb') as f:
    f.read(80)
    data=f.read(4)
tri=struct.unpack('<I',data)[0] if len(data)==4 else 0
print('File:',p.name)
print('Size:',p.stat().st_size)
print('Triangles:',tri)
