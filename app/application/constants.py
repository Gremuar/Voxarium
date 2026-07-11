"""
Voxarium
Application constants.

В этом модуле располагаются только константы приложения.

Правило:
    Если значение потенциально может изменяться пользователем,
    оно не должно находиться в этом файле.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

#
# -----------------------------------------------------------------------------
# Информация о приложении
# -----------------------------------------------------------------------------
#

APP_NAME: Final[str] = "Voxarium"

APP_VERSION: Final[str] = "0.1.0"

APP_DESCRIPTION: Final[str] = (
    "Offline modular platform for speech synthesis."
)

APP_AUTHOR: Final[str] = "Gremuar"

APP_LICENSE: Final[str] = "MIT"

#
# -----------------------------------------------------------------------------
# Каталоги проекта
# -----------------------------------------------------------------------------
#

DATA_DIRECTORY: Final[Path] = Path("data")

CACHE_DIRECTORY: Final[Path] = DATA_DIRECTORY / "cache"

DATABASE_DIRECTORY: Final[Path] = DATA_DIRECTORY / "database"

LOG_DIRECTORY: Final[Path] = DATA_DIRECTORY / "logs"

OUTPUT_DIRECTORY: Final[Path] = DATA_DIRECTORY / "output"

TEMP_DIRECTORY: Final[Path] = DATA_DIRECTORY / "temp"

VOICE_DIRECTORY: Final[Path] = DATA_DIRECTORY / "voices"

ENGINE_DIRECTORY: Final[Path] = DATA_DIRECTORY / "engines"

PROJECT_DIRECTORY: Final[Path] = DATA_DIRECTORY / "projects"

MODEL_DIRECTORY: Final[Path] = DATA_DIRECTORY / "models"

PRESET_DIRECTORY: Final[Path] = DATA_DIRECTORY / "presets"

IMPORT_DIRECTORY: Final[Path] = DATA_DIRECTORY / "imports"

EXPORT_DIRECTORY: Final[Path] = DATA_DIRECTORY / "exports"

#
# -----------------------------------------------------------------------------
# База данных
# -----------------------------------------------------------------------------
#

DATABASE_FILENAME: Final[str] = "voxarium.db"

DATABASE_FILE: Final[Path] = (
    DATABASE_DIRECTORY / DATABASE_FILENAME
)

#
# -----------------------------------------------------------------------------
# Web API
# -----------------------------------------------------------------------------
#

DEFAULT_HOST: Final[str] = "127.0.0.1"

DEFAULT_PORT: Final[int] = 8000

DEFAULT_API_PREFIX: Final[str] = "/api"

#
# -----------------------------------------------------------------------------
# Поддерживаемые форматы документов
# -----------------------------------------------------------------------------
#

SUPPORTED_DOCUMENT_EXTENSIONS: Final[tuple[str, ...]] = (
    ".txt",
    ".md",
    ".pdf",
    ".doc",
    ".docx",
)

#
# -----------------------------------------------------------------------------
# Поддерживаемые аудиоформаты
# -----------------------------------------------------------------------------
#

SUPPORTED_AUDIO_EXTENSIONS: Final[tuple[str, ...]] = (
    ".wav",
    ".mp3",
    ".flac",
    ".ogg",
    ".opus",
    ".m4a",
)

#
# -----------------------------------------------------------------------------
# Форматы импорта голосов
# -----------------------------------------------------------------------------
#

SUPPORTED_VOICE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".wav",
    ".mp3",
    ".flac",
)

#
# -----------------------------------------------------------------------------
# Движки синтеза речи
# -----------------------------------------------------------------------------
#

ENGINE_EDGE_TTS: Final[str] = "edge-tts"

ENGINE_XTTS: Final[str] = "xtts-v2"

#
# -----------------------------------------------------------------------------
# Настройки по умолчанию
# -----------------------------------------------------------------------------
#

DEFAULT_SPEECH_RATE: Final[float] = 1.0

DEFAULT_SPEECH_PITCH: Final[float] = 1.0

DEFAULT_OUTPUT_FORMAT: Final[str] = "mp3"

DEFAULT_ENGINE: Final[str] = ENGINE_EDGE_TTS

#
# -----------------------------------------------------------------------------
# Прочее
# -----------------------------------------------------------------------------
#

UTF8: Final[str] = "utf-8"

SECONDS_IN_MINUTE: Final[int] = 60

MILLISECONDS_IN_SECOND: Final[int] = 1000

BYTES_IN_MEGABYTE: Final[int] = 1024 * 1024


__all__ = [
    "APP_NAME",
    "APP_VERSION",
    "APP_DESCRIPTION",
    "APP_AUTHOR",
    "APP_LICENSE",
    "DATA_DIRECTORY",
    "CACHE_DIRECTORY",
    "DATABASE_DIRECTORY",
    "LOG_DIRECTORY",
    "OUTPUT_DIRECTORY",
    "TEMP_DIRECTORY",
    "VOICE_DIRECTORY",
    "ENGINE_DIRECTORY",
    "PROJECT_DIRECTORY",
    "MODEL_DIRECTORY",
    "PRESET_DIRECTORY",
    "IMPORT_DIRECTORY",
    "EXPORT_DIRECTORY",
    "DATABASE_FILENAME",
    "DATABASE_FILE",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_API_PREFIX",
    "SUPPORTED_DOCUMENT_EXTENSIONS",
    "SUPPORTED_AUDIO_EXTENSIONS",
    "SUPPORTED_VOICE_EXTENSIONS",
    "ENGINE_EDGE_TTS",
    "ENGINE_XTTS",
    "DEFAULT_SPEECH_RATE",
    "DEFAULT_SPEECH_PITCH",
    "DEFAULT_OUTPUT_FORMAT",
    "DEFAULT_ENGINE",
    "UTF8",
]