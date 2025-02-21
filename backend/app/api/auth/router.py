from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login")
async def login():
    return {"message": "Hello World"}
