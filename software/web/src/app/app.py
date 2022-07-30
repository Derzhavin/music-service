from fastapi import FastAPI

from configs.Environment import get_environment_variables
from models.BaseModel import init
from routes.index import IndexRouter


def create_app():
    env = get_environment_variables()

    app = FastAPI(
        title=env.APP_NAME,
        version=env.API_VERSION,
    )
    app.include_router(IndexRouter)

    init()

    return app


app = create_app()