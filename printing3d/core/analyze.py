from pathlib import Path
from printing3d.core.model_info import ModelInfo
from printing3d.validators.kobra import fits

def analyze(path):
    p=Path(path)
    size=p.stat().st_size
    dims=(0.0,0.0,0.0)  # placeholder until trimesh integration
    return ModelInfo(
        filename=p.name,
        filetype=p.suffix.lower(),
        size_bytes=size,
        dimensions_mm=dims,
        estimated_volume_cm3=0.0,
        estimated_weight_g=0.0,
        compatible_kobra_x=fits(*dims)
    )
