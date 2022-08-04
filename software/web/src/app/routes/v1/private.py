from fastapi import APIRouter, Depends
from .auth import get_current_user

PrivateRouter = APIRouter(prefix='/private')


@PrivateRouter.get("/")
async def private(username: str = Depends(get_current_user)):
    return username
