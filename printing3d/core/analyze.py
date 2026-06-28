from pathlib import Path

def analyze(path):
    p=Path(path)
    ext=p.suffix.lower()
    return {
      "file":p.name,
      "type":ext,
      "size_bytes":p.stat().st_size,
      "status":"Prototype analyzer"
    }
