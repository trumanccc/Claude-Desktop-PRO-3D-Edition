from printing3d.core.model_info import ModelInfo
def export(info:ModelInfo):
    return f'''# 3D Analysis Report

- File: {info.filename}
- Type: {info.filetype}
- Size: {info.size_bytes} bytes
- Dimensions: {info.dimensions_mm}
- Estimated volume: {info.estimated_volume_cm3} cm³
- Estimated weight: {info.estimated_weight_g} g
- Fits Kobra X: {info.compatible_kobra_x}
'''
