from pathlib import Path
import sys
if len(sys.argv)!=2: raise SystemExit('Usage: python gcode_analyzer.py file.gcode')
lines=Path(sys.argv[1]).read_text(errors='ignore').splitlines()
print('Lines:',len(lines))
print('M104/M109:',sum(1 for l in lines if l.startswith('M104') or l.startswith('M109')))
