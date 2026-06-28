from pathlib import Path
from printing3d.models import AnalysisResult

def analyze(path:str)->AnalysisResult:
    p=Path(path)
    return AnalysisResult(
        filename=p.name,
        filetype="STL",
        size_bytes=p.stat().st_size,
        notes=["Geometry analysis planned for v0.6"]
    )
