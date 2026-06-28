"""Wrapper preparado para integrar trimesh.

En esta versión usa una implementación de reserva cuando trimesh
no está instalado.
"""

from pathlib import Path

try:
    import trimesh
except ImportError:
    trimesh=None

def analyze_mesh(path):
    p=Path(path)
    if trimesh is None:
        return {
            "engine":"fallback",
            "file":p.name,
            "size_bytes":p.stat().st_size,
            "dimensions_mm":None,
            "volume_cm3":None,
            "surface_area_mm2":None
        }

    mesh=trimesh.load(p,force="mesh")
    extents=mesh.bounding_box.extents.tolist()
    volume=mesh.volume/1000.0
    area=mesh.area
    return {
        "engine":"trimesh",
        "file":p.name,
        "size_bytes":p.stat().st_size,
        "dimensions_mm":[round(x,2) for x in extents],
        "volume_cm3":round(volume,2),
        "surface_area_mm2":round(area,2)
    }
