from pydantic import BaseModel
from backend.utils.env_utils import load_config


class AppConfig(BaseModel):
    root_path: str
    developer_mode: bool
    uvicorn_server_port: int

    routers_root_path: str
    music_types: list

    notes_path: str
    weights_path: str
    results_file_path: str
    sound_font_path: str

    @classmethod
    def load_config(cls) -> 'AppConfig':
        data_env = load_config()
        music_types: list = ['piano', 'guitar', 'lol']
        return AppConfig(
            root_path=data_env.get('APP_ROOT_PATH', ''),
            uvicorn_server_port=data_env.get('UVICORN_SERVER_PORT', 4000),
            developer_mode=data_env.get('DEVELOPER_MODE') == 'true',
            routers_root_path=data_env.get('ROUTERS_ROOT_PATH', ''),
            music_types=music_types,
            notes_path=data_env.get('NOTES_PATH', 'neural_network_data/data/notes'),
            weights_path=data_env.get('WEIGHTS_PATH', 'neural_network_data/weights/weights.hdf5'),
            results_file_path=data_env.get('RESULTS_FILE_PATH', 'neural_network_data/results'),
            sound_font_path=data_env.get('SOUND_FONT_PATH', 'fluidsynth/default_sound_font.sf2')
        )


config = AppConfig.load_config()


def get_app_config() -> AppConfig:
    return config
