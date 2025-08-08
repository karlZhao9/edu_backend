from fastapi import APIRouter

router = APIRouter(tags=["v1-系统状态"])


@router.get("/health")
async def health_check():
    return {"status": "ok"}
