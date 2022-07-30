from fastapi import APIRouter

IndexRouter = APIRouter()


@IndexRouter.get("/")
async def root():
    return {"message": "Aloha!"}