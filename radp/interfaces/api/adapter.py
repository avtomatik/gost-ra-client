from fastapi import APIRouter, Depends

from radp.runtime import Runtime

from .runtime import get_runtime

router = APIRouter(prefix="/adapter", tags=["adapter"])


@router.get("/certificates")
def certificates(runtime: Runtime = Depends(get_runtime)):
    return runtime.client.list_first_page().model_dump(by_alias=True)


@router.get("/certificates/{certificate_id}")
def get_certificate_by_id(
    certificate_id: str, runtime: Runtime = Depends(get_runtime)
):
    return runtime.client.get_certificate(certificate_id)


@router.get("/certificates/search")
def search_certificates(q: str, runtime: Runtime = Depends(get_runtime)):
    return runtime.client.search_certificates(q)
