from pathlib import Path
import yaml

DEFAULT=Path(__file__).resolve().parents[2]/"config"/"settings.yaml"

def load(path=None):
    cfg=Path(path) if path else DEFAULT
    with cfg.open("r",encoding="utf8") as f:
        return yaml.safe_load(f)
