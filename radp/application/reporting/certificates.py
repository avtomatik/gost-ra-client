from datetime import datetime, timezone

from radp.application.reporting.models import ReportArtifact
from radp.config.paths import EXPORTS_DIR
from radp.infrastructure.persistence.repositories.snapshot_repository import \
    SnapshotRepository

from .projection import CertificateProjection
from .xlsx import XLSXExporter


class CertificateReportService:
    def __init__(
        self, snapshots: SnapshotRepository, exporter: XLSXExporter
    ) -> None:
        self.snapshots = snapshots
        self.exporter = exporter

    def export_excel(self) -> ReportArtifact:
        generated_at = datetime.now(timezone.utc)
        filename = f"certificates_inventory_{generated_at:%Y-%m-%d-%H-%M}.xlsx"
        path = EXPORTS_DIR / filename

        snapshots = self.snapshots.list_all()
        rows = [
            CertificateProjection.inventory(snapshot) for snapshot in snapshots
        ]
        self.exporter.export(rows, path, sheet_name="certificates_inventory")

        return ReportArtifact(
            name="certificates_inventory", generated_at=generated_at, path=path
        )
