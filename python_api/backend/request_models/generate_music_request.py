from datetime import date
from fastapi import Query
from enum import IntEnum
from pydantic import BaseModel, validator

from backend.core.config.app_config import get_app_config

config = get_app_config()


class GenerateMusicRequest(BaseModel):
    notes_count: int
    music_type: str

    @validator('music_type')
    def validate_music_type(cls, v, values):

        if v not in config.music_types:
            raise ValueError(f'Music type should be in: {config.music_types}')
