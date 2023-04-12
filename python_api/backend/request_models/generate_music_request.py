from enum import Enum
from pydantic import BaseModel

from backend.core.config.app_config import get_app_config

config = get_app_config()


class MusicType(str, Enum):
    ELECTRO_PIANO = 'electro_piano'
    CLASSIC_PIANO = 'classic_piano'
    GUITAR = 'guitar'
    SUPER_GAME_BOY = 'super_game_boy'


class GenerateMusicRequest(BaseModel):
    notes_count: int
    music_type: MusicType
