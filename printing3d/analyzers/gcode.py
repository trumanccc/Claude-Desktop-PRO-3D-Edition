from pathlib import Path
from printing3d.models import AnalysisResult

def analyze(path:str)->AnalysisResult:
    p=Path(path)
    return AnalysisResult(
        filename=p.name,
        filetype="GCODE",
        size_bytes=p.stat().st_size,
        notes=["Basic parser"]
    )
