"""
Voxarium.

Пакет инфраструктуры приложения.

Через данный пакет экспортируются основные объекты,
необходимые для запуска приложения.
"""

from app.application.application import Application
from app.application.constants import (
    APP_AUTHOR,
    APP_DESCRIPTION,
    APP_LICENSE,
    APP_NAME,
    APP_VERSION,
)
from app.application.logger import (
    configure_logger,
    get_logger,
    is_logger_configured,
    shutdown_logger,
)
from app.application.paths import Paths

__all__ = [
    "Application",
    "APP_AUTHOR",
    "APP_DESCRIPTION",
    "APP_LICENSE",
    "APP_NAME",
    "APP_VERSION",
    "configure_logger",
    "get_logger",
    "is_logger_configured",
    "shutdown_logger",
    "Paths",
]