from rads_explorer.certificate_domain.models.certificate import Certificate

from .cache import SnapshotCache
from .certificate_snapshot import CertificateSnapshot
from .factory import CertificateSnapshotFactory


class SnapshotProvider:
    def __init__(
        self, cache: SnapshotCache, factory: CertificateSnapshotFactory
    ):
        self._cache = cache
        self._factory = factory

    def get_or_create(self, certificate: Certificate) -> CertificateSnapshot:
        cached = self._cache.get(certificate.id)
        if cached:
            return cached
        snapshot = self._factory.create(certificate)
        self._cache.put(snapshot)
        return snapshot
