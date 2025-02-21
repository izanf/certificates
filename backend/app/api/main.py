from fastapi import APIRouter

from app.api.auth.router import router as auth_router
from app.api.utils import router as utils_router
# from app.core.config import settings

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(utils_router)

# if settings.ENVIRONMENT == "local":
#     api_router.include_router(private.router)
