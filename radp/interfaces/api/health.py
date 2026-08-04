from fastapi import APIRouter, Depends

from radp.runtime import Runtime

from .runtime import get_runtime

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health(runtime: Runtime = Depends(get_runtime)):
    settings = runtime.settings
    return {
        "status": "ok",
        "transport": settings.transport,
        "api_base_url": str(settings.api_base_url),
        "curl_path": str(settings.curl_path),
        "cert_thumbprint_set": bool(settings.cert_thumbprint),
        "database": settings.database_driver,
    }
