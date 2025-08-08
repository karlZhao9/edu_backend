from fastapi import APIRouter
from modules.auth.service import create_user
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["v1-用户认证"])


@router.post("/register", response_model=UserCreate)
async def register(user: UserCreate):
    return create_user(user.username, user.password)
