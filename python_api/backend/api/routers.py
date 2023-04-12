from fastapi import APIRouter, FastAPI

from backend.core.config.app_config import get_app_config
from backend.core.containers import inject_module
from backend.routers.generate_music.generate_music_router import generate_music_router

inject_module(__name__)

router = APIRouter(
    tags=['mars-epms-backend'],
)

config = get_app_config()


def add_routers(app: FastAPI):
    routers = [
        generate_music_router,
    ]
    _add_routers(app, routers)


def _add_routers(app: FastAPI, routers: list[APIRouter]):
    for rout in routers:
        app.include_router(rout)
