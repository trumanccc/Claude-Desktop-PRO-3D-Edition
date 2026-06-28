from pathlib import Path
import struct
def analyze(path):
 p=Path(path)
 with p.open('rb') as f:
  hdr=f.read(80)
  ascii=hdr.lower().startswith(b'solid')
  tri=None
  if not ascii:
   d=f.read(4)
   tri=struct.unpack('<I',d)[0] if len(d)==4 else None
 return {'file':p.name,'format':'ASCII' if ascii else 'Binary','size':p.stat().st_size,'triangles':tri}
