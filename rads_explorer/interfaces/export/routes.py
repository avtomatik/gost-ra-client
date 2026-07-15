from datetime import datetime
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from rads_explorer.config.paths import EXPORTS_DIR
from rads_explorer.container.container import get_container

router = APIRouter(prefix="/export", tags=["EXPORT"])


@router.get("/inventory")
def export_certificates_inventory():
    container = get_container()
    report_service = container.report_service()

    report = report_service.certificates_inventory_report()
    output = Path("/tmp/certificates_inventory.xlsx")

    container.exporter().export(report, output)
    return FileResponse(
        output,
        filename=f"certificates_inventory_{datetime.now():%Y-%m-%d-%H-%M}.xlsx",
    )


@router.get("/expiring")
def export_expiring(days: int = 30):
    container = get_container()
    report_service = container.report_service()
    report = report_service.expiring_certificates_report(days)
    path = EXPORTS_DIR / "expiring.xlsx"
    container.exporter().export(report, path)
    return {"file": str(path)}
