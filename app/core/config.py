from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseModel):
    language: str = "ru"
    theme: str = "light"


class TTSSettings(BaseModel):
    default_engine: str = ""
    default_voice: str = ""
    speed: float = Field(default=1.0, ge=0.25, le=3.0)
    pitch: float = Field(default=1.0, ge=0.5, le=2.0)


class PathsSettings(BaseModel):
    output: Path = Path("data/output")
    voices: Path = Path("data/voices")
    cache: Path = Path("data/cache")
    temp: Path = Path("data/temp")
    engines: Path = Path("data/engines")
    logs: Path = Path("data/logs")


class SystemSettings(BaseModel):
    gpu: bool = True
    ffmpeg: str = ""
    workers: int = Field(default=2, ge=1, le=64)


class Settings(BaseSettings):

    application: ApplicationSettings = ApplicationSettings()

    tts: TTSSettings = TTSSettings()

    paths: PathsSettings = PathsSettings()

    system: SystemSettings = SystemSettings()

    model_config = SettingsConfigDict(
        env_prefix="TTS_",
        extra="ignore"
    )


settings = Settings()


def create_directories() -> None:
    """
    Создает необходимые каталоги проекта.
    """

    for directory in (
        settings.paths.output,
        settings.paths.voices,
        settings.paths.cache,
        settings.paths.temp,
        settings.paths.engines,
        settings.paths.logs,
    ):
        directory.mkdir(parents=True, exist_ok=True)