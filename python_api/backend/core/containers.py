from typing import Set
from dependency_injector import containers

from python_api.backend.core.containers_utils.base import get_di_config

modules: Set = set()


class Container(containers.DeclarativeContainer):
    # Base
    app_config = get_di_config()
    # database = get_database(providers, config)

    # services


container = Container()


def inject_module(module_name: str):
    modules.add(module_name)


def wire_modules():
    container.wire(modules=list(modules))
