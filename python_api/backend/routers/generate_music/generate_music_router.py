from fastapi import Depends
from fastapi.responses import FileResponse
from dependency_injector.wiring import inject, Provide

from backend.core.containers import Container, inject_module
from backend.request_models.generate_music_request import GenerateMusicRequest
from backend.routers.custom_api_router import CustomApiRouter


from backend.services.lstm_music_generator_service import LSTMMusicGeneratorService

inject_module(__name__)

generate_music_router = CustomApiRouter(
    tags=['music-generator'],
)


@generate_music_router.get(
    '/generate_music',
)
@inject
async def generate_music(
    request_data: GenerateMusicRequest = Depends(),
    service: LSTMMusicGeneratorService = Depends(
        Provide[Container.music_generator_service],
    ),
):
    return service.generate_music(request_data)
    # return service.generate_music(request_data)
