from fastapi import APIRouter, FastAPI

from python_api.backend.core.config.app_config import get_app_config
from python_api.backend.core.containers import inject_module

inject_module(__name__)

router = APIRouter(
    tags=['mars-epms-backend'],
)

config = get_app_config()


def add_routers(app: FastAPI):
    routers = [
    ]
    _add_routers(app, routers)


def _add_routers(app: FastAPI, routers: list[APIRouter]):
    for rout in routers:
        app.include_router(rout)
