from backend.services.lstm_music_generator_service import LSTMMusicGeneratorService


def get_music_generator_service(
    providers,
    config,
) -> LSTMMusicGeneratorService:
    return providers.Factory(
        LSTMMusicGeneratorService,
        config=config,
    )
