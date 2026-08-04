from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from radp.runtime import Runtime

from .runtime import get_runtime

router = APIRouter(prefix="/export", tags=["export"])


@router.get("/certificates")
def export_certificates(runtime: Runtime = Depends(get_runtime)):
    report = runtime.reporting.export_excel()
    return FileResponse(report.path)
