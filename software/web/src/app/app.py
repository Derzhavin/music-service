from fastapi import FastAPI

from .configs.Environment import get_environment_variables
from .models.domain.BaseModel import init_db
from .routes.v1 import IndexRouter, PrivateRouter, SecurityRouter


def create_app():
    env = get_environment_variables()

    app = FastAPI(
        title=env.APP_NAME,
        version=env.API_VERSION,
    )
    app.include_router(IndexRouter)
    app.include_router(PrivateRouter)
    app.include_router(SecurityRouter)

    init_db()

    return app


app = create_app()