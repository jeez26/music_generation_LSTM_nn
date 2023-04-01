from typing import Set
from dependency_injector import containers, providers

from backend.core.containers_utils.base import get_di_config
from backend.core.containers_utils.music_generator_service import get_music_generator_service

modules: Set = set()


class Container(containers.DeclarativeContainer):
    # Base
    app_config = get_di_config()
    # database = get_database(providers, config)

    # services
    music_generator_service = get_music_generator_service(providers)


container = Container()


def inject_module(module_name: str):
    print('there')
    modules.add(module_name)


def wire_modules():
    print(list(modules))
    container.wire(modules=list(modules))
