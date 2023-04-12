from fastapi import APIRouter

from backend.core.config.app_config import get_app_config


class CustomApiRouter(APIRouter):
    config = get_app_config()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = self.config.routers_root_path
