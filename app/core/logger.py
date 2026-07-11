"""
Единая система логирования приложения.

Все компоненты проекта должны получать логгер только через get_logger().
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "tts_studio.log"


_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)-20s | "
    "%(message)s"
)


def _create_root_logger() -> None:
    root = logging.getLogger()

    if root.handlers:
        return

    root.setLevel(logging.INFO)

    formatter = logging.Formatter(_FORMAT)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root.addHandler(console)
    root.addHandler(file_handler)


_create_root_logger()


def get_logger(name: str) -> logging.Logger:
    """
    Возвращает логгер указанного компонента.

    Parameters
    ----------
    name:
        Имя компонента.

    Returns
    -------
    logging.Logger
    """
    return logging.getLogger(name)