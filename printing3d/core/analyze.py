from printing3d.engines.trimesh_engine import analyze_mesh
from printing3d.validators.kobra import fits

def analyze(path):
    data=analyze_mesh(path)
    dims=data.get("dimensions_mm")
    if dims:
        data["fits_kobra_x"]=fits(*dims)
    else:
        data["fits_kobra_x"]=None
    return data
