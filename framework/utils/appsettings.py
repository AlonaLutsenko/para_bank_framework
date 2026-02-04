import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict


@lru_cache(maxsize=1)
def load_appsettings() -> Dict[str, Any]:
    root = Path(__file__).resolve().parents[2]
    settings_path = root / "appsettings.json"
    if not settings_path.exists():
        return {}
    return json.loads(settings_path.read_text(encoding="utf-8"))


def get_setting(*keys: str, default: Any = None) -> Any:
    settings = load_appsettings()
    current: Any = settings
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def get_profile(profile: str) -> Dict[str, Any]:
    return get_setting("profiles", profile, default={})
