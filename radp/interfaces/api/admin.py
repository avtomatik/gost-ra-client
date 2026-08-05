from fastapi import APIRouter, Depends

from radp.runtime import Runtime

from .runtime import get_runtime

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/certificates/sync")
def synchronize(runtime: Runtime = Depends(get_runtime)):
    count = runtime.synchronization.synchronize()
    return {"synchronized": count}
