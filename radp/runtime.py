import logging

from radp.application.reporting.certificates import CertificateReportService
from radp.application.reporting.xlsx import XLSXExporter
from radp.application.synchronization.certificates import \
    CertificateSynchronizationService
from radp.config.settings import Settings
from radp.domain.snapshots.decoder import CertificateDecoder
from radp.domain.snapshots.factory import CertificateSnapshotFactory
from radp.infrastructure.persistence.bootstrap import build_persistence
from radp.infrastructure.persistence.repositories.oid_repository import \
    OIDRepository
from radp.infrastructure.persistence.repositories.snapshot_repository import \
    SnapshotRepository
from radp.infrastructure.ra_api.client import RAClient
from radp.infrastructure.transport.factory import create_transport
from radp.oid_registry.bootstrap import OIDRegistryBootstrap

logger = logging.getLogger(__name__)


class Runtime:
    def __init__(self) -> None:
        self.settings = Settings()
        # =====================================================================
        # Persistence
        # =====================================================================
        self.session_factory = build_persistence(self.settings)
        self.oid_repository = OIDRepository(self.session_factory)
        self.snapshot_repository = SnapshotRepository(self.session_factory)
        # =====================================================================
        # Bootstrap registry
        # =====================================================================
        OIDRegistryBootstrap(self.oid_repository).initialize()
        # =====================================================================
        # Transport / RA API
        # =====================================================================
        self.transport = create_transport(self.settings)
        self.client = RAClient(self.transport)
        # =====================================================================
        # Domain services
        # =====================================================================
        self.snapshot_factory = CertificateSnapshotFactory(
            oid_repository=self.oid_repository, decoder=CertificateDecoder()
        )
        # =====================================================================
        # Application services
        # =====================================================================
        self.synchronization = CertificateSynchronizationService(
            client=self.client,
            snapshots=self.snapshot_repository,
            factory=self.snapshot_factory,
        )
        self.reporting = CertificateReportService(
            snapshots=self.snapshot_repository,
            exporter=XLSXExporter(),
        )
        logger.info("Runtime initialized")
        logger.info("Transport=%s", self.settings.transport)
        logger.info("Database=%s", self.settings.database_url)
