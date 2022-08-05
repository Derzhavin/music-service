from fastapi import APIRouter, Depends
from .security import get_current_user

PrivateRouter = APIRouter(prefix='/v1/users')


@PrivateRouter.get("/private", tags=['users'])
async def private(username: str = Depends(get_current_user)):
    return username
