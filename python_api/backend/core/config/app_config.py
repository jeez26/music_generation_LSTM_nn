from pydantic import BaseModel
from python_api.backend.utils.env_utils import load_config


class AppConfig(BaseModel):
    root_path: str
    developer_mode: bool
    uvicorn_server_port: int

    @classmethod
    def load_config(cls) -> 'AppConfig':
        data_env = load_config()
        return AppConfig(
            root_path=data_env.get('APP_ROOT_PATH', ''),
            uvicorn_server_port=data_env.get('UVICORN_SERVER_PORT', 3000),
            developer_mode=data_env.get('DEVELOPER_MODE') == 'true',
        )


config = AppConfig.load_config()


def get_app_config() -> AppConfig:
    return config
