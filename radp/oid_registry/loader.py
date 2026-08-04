import json
from pathlib import Path

from .models import OIDDefinition


class OIDRegistryLoader:
    def load(self, fixture_path: Path) -> list[OIDDefinition]:
        if not fixture_path.exists():
            return []
        with fixture_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if not isinstance(payload, list):
            raise ValueError("OID registry fixture must contain a JSON array")
        return [OIDDefinition.model_validate(item) for item in payload]
