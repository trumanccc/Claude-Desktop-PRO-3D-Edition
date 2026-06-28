from printing3d.models import AnalysisResult

def export(result:AnalysisResult)->str:
    return f"""# Analysis Report

- File: {result.filename}
- Type: {result.filetype}
- Size: {result.size_bytes} bytes

## Notes
""" + "\n".join(f"- {n}" for n in result.notes)
