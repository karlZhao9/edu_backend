from fastapi import FastAPI
from app.api.v1.auth import router as v1_auth_router
from app.api.v1.health import router as v1_health_router

app = FastAPI()

# 挂载v1路由组
app.include_router(v1_auth_router, prefix="/api/v1")
app.include_router(v1_health_router, prefix="/api/v1")

# 未来扩展v2
# app.include_router(v2_auth_router, prefix="/api/v2")
