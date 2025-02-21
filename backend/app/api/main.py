from fastapi import APIRouter

from app.api.auth.router import auth_router
# from app.core.config import settings

api_router = APIRouter()
api_router.include_router(auth_router)

# if settings.ENVIRONMENT == "local":
#     api_router.include_router(private.router)
