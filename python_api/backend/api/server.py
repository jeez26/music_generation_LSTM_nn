from fastapi import FastAPI

from python_api.backend.api.docs_router import docs_router
from python_api.backend.api.routers import add_routers


def create_api_server() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
    )

    add_routers(app)
    docs_router(app)

    return app
