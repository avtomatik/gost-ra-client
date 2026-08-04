from pathlib import Path

from radp.config.paths import OID_REGISTRY_FIXTURE_PATH

from .loader import OIDRegistryLoader


class OIDRegistryBootstrap:
    def __init__(self, repository, loader: OIDRegistryLoader | None = None):
        self.repository = repository
        self.loader = loader or OIDRegistryLoader()

    def initialize(self, fixture_path: Path | None = None) -> int:
        path = fixture_path or OID_REGISTRY_FIXTURE_PATH
        definitions = self.loader.load(path)
        inserted = 0
        for definition in definitions:
            if self.repository.exists(definition.oid):
                continue
            self.repository.save(definition)
            inserted += 1
        return inserted
