from fastapi import FastAPI

from backend.api.docs_router import docs_router
from backend.api.routers import add_routers


def create_api_server() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
    )

    add_routers(app)
    docs_router(app)

    return app
