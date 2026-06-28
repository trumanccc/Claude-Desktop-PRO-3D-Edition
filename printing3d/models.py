from dataclasses import dataclass

@dataclass
class AnalysisResult:
    filename:str
    filetype:str
    size_bytes:int
    notes:list[str]
