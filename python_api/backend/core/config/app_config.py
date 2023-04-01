from pydantic import BaseModel
from backend.utils.env_utils import load_config


class AppConfig(BaseModel):
    root_path: str
    developer_mode: bool
    uvicorn_server_port: int

    routers_root_path: str
    music_types: list

    @classmethod
    def load_config(cls) -> 'AppConfig':
        data_env = load_config()
        music_types: list = ['piano', 'guitar', 'lol']
        return AppConfig(
            root_path=data_env.get('APP_ROOT_PATH', ''),
            uvicorn_server_port=data_env.get('UVICORN_SERVER_PORT', 3000),
            developer_mode=data_env.get('DEVELOPER_MODE') == 'true',
            routers_root_path=data_env.get('ROUTERS_ROOT_PATH', ''),
            music_types=music_types,
        )


config = AppConfig.load_config()


def get_app_config() -> AppConfig:
    return config
