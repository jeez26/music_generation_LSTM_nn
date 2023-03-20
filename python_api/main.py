import uvicorn

from backend.api.server import create_api_server
from backend.core.config.app_config import AppConfig
from backend.core.containers import wire_modules

backend = create_api_server()
wire_modules()

config = AppConfig.load_config()

if __name__ == '__main__':
    uvicorn.run(
        'main:backend',
        host='localhost',
        port=config.uvicorn_server_port,
        reload=config.developer_mode,
    )
