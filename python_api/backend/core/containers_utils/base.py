from python_api.backend.core.config.app_config import get_app_config, AppConfig
#from database.db import AsyncDb


def get_di_config() -> AppConfig:
    return get_app_config()


# def get_database(providers, config: AppConfig):
#     return providers.Singleton(
#         AsyncDb,
#         db_url=config.db_url,
#         debug=config.debug,
#     )
