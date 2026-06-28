from dataclasses import dataclass
@dataclass
class ModelInfo:
    filename:str
    filetype:str
    size_bytes:int
    dimensions_mm:tuple[float,float,float]|None=None
    estimated_volume_cm3:float|None=None
    estimated_weight_g:float|None=None
    compatible_kobra_x:bool|None=None
