"""
Voxarium
Project paths.

Централизованное управление путями проекта.
"""

from __future__ import annotations

from pathlib import Path

from app.application.constants import (
    CACHE_DIRECTORY,
    DATABASE_DIRECTORY,
    DATABASE_FILE,
    ENGINE_DIRECTORY,
    EXPORT_DIRECTORY,
    IMPORT_DIRECTORY,
    LOG_DIRECTORY,
    MODEL_DIRECTORY,
    OUTPUT_DIRECTORY,
    PRESET_DIRECTORY,
    PROJECT_DIRECTORY,
    TEMP_DIRECTORY,
    VOICE_DIRECTORY,
)


class Paths:
    """
    Централизованный доступ к каталогам проекта.

    Все остальные модули должны использовать Paths,
    а не обращаться к pathlib.Path напрямую.
    """

    cache: Path = CACHE_DIRECTORY

    database: Path = DATABASE_DIRECTORY

    engines: Path = ENGINE_DIRECTORY

    exports: Path = EXPORT_DIRECTORY

    imports: Path = IMPORT_DIRECTORY

    logs: Path = LOG_DIRECTORY

    models: Path = MODEL_DIRECTORY

    output: Path = OUTPUT_DIRECTORY

    presets: Path = PRESET_DIRECTORY

    projects: Path = PROJECT_DIRECTORY

    temp: Path = TEMP_DIRECTORY

    voices: Path = VOICE_DIRECTORY

    database_file: Path = DATABASE_FILE

    @classmethod
    def create_directories(cls) -> None:
        """
        Создает структуру каталогов приложения.

        Метод безопасен для повторного вызова.
        """

        for directory in (
            cls.cache,
            cls.database,
            cls.engines,
            cls.exports,
            cls.imports,
            cls.logs,
            cls.models,
            cls.output,
            cls.presets,
            cls.projects,
            cls.temp,
            cls.voices,
        ):
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

    @classmethod
    def exists(cls) -> bool:
        """
        Проверяет существование всех каталогов.

        Returns
        -------
        bool
            True, если структура каталогов существует.
        """

        return all(
            directory.exists()
            for directory in (
                cls.cache,
                cls.database,
                cls.engines,
                cls.exports,
                cls.imports,
                cls.logs,
                cls.models,
                cls.output,
                cls.presets,
                cls.projects,
                cls.temp,
                cls.voices,
            )
        )

    @classmethod
    def ensure(cls) -> None:
        """
        Гарантирует существование структуры каталогов.
        """

        if not cls.exists():
            cls.create_directories()

    @classmethod
    def resolve(cls, path: str | Path) -> Path:
        """
        Возвращает абсолютный путь.

        Parameters
        ----------
        path
            Относительный или абсолютный путь.

        Returns
        -------
        Path
        """

        return Path(path).expanduser().resolve()

    @classmethod
    def relative_to_project(cls, path: str | Path) -> Path:
        """
        Возвращает путь относительно каталога проекта.

        Если путь невозможно сделать относительным,
        возвращается исходный путь.

        Parameters
        ----------
        path
            Исходный путь.

        Returns
        -------
        Path
        """

        path = cls.resolve(path)

        try:
            return path.relative_to(Path.cwd())
        except ValueError:
            return path


__all__ = [
    "Paths",
]