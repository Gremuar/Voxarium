"""
Voxarium.

Главный класс приложения.

Application отвечает за:

- жизненный цикл приложения;
- инициализацию инфраструктуры;
- создание контейнера сервисов;
- создание экземпляра FastAPI;
- запуск и остановку приложения.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any
from typing import AsyncIterator

from fastapi import FastAPI

from app.application.constants import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_VERSION,
)
from app.application.logger import LoggerManager
from app.application.paths import Paths


class Application:
    """
    Главный объект приложения Voxarium.

    В приложении должен существовать только один экземпляр
    данного класса.
    """

    def __init__(self) -> None:
        self._initialized = False

        #
        # Контейнер сервисов.
        #
        self._services: dict[type, Any] = {}

        #
        # Логгер будет создан во время initialize().
        #
        self._logger: LoggerManager | None = None

        self._api = FastAPI(
            title=APP_NAME,
            description=APP_DESCRIPTION,
            version=APP_VERSION,
            docs_url="/docs",
            redoc_url="/redoc",
            lifespan=self._lifespan,
        )

    @property
    def api(self) -> FastAPI:
        """
        Возвращает экземпляр FastAPI.
        """

        return self._api

    @property
    def initialized(self) -> bool:
        """
        Возвращает состояние приложения.
        """

        return self._initialized

    def initialize(self) -> None:
        """
        Выполняет инициализацию приложения.

        Метод безопасен для повторного вызова.
        """

        if self._initialized:
            return

        Paths.ensure()

        logger = LoggerManager(
            log_directory=Paths.logs,
            debug=False,
        )

        logger.configure()

        self._logger = logger

        self._logger.get_logger(__name__).info(
            "Initializing application..."
        )

        self._register_core_services()

        self._initialized = True

        self._logger.get_logger(__name__).success(
            "Application initialized."
        )
        
    def shutdown(self) -> None:
        """
        Корректно завершает работу приложения.

        Метод безопасен для повторного вызова.
        """

        if not self._initialized:
            return

        if self._logger is not None:
            log = self._logger.get_logger(__name__)
            log.info("Shutting down application...")

        #
        # Останавливаем зарегистрированные сервисы
        # в порядке, обратном регистрации.
        #
        for service in reversed(list(self._services.values())):
            shutdown = getattr(service, "shutdown", None)

            if callable(shutdown):
                try:
                    shutdown()
                except Exception:
                    if self._logger is not None:
                        self._logger.get_logger(__name__).exception(
                            "Service shutdown failed."
                        )

        self._services.clear()

        if self._logger is not None:
            self._logger.get_logger(__name__).info(
                "Application stopped."
            )

            self._logger.shutdown()
            self._logger = None

        self._initialized = False

    def register_service(
        self,
        service: object,
    ) -> None:
        """
        Регистрирует сервис в контейнере.

        Parameters
        ----------
        service
            Экземпляр сервиса.
        """

        self._services[type(service)] = service

    def get_service(
        self,
        service_type: type,
    ) -> object:
        """
        Возвращает зарегистрированный сервис.

        Raises
        ------
        KeyError
            Если сервис отсутствует.
        """

        return self._services[service_type]

    def has_service(
        self,
        service_type: type,
    ) -> bool:
        """
        Проверяет наличие сервиса.
        """

        return service_type in self._services

    def _register_core_services(self) -> None:
        """
        Регистрирует базовые сервисы приложения.

        На первом этапе регистрируется только LoggerManager.
        Остальные сервисы будут добавляться по мере разработки.
        """

        if self._logger is None:
            raise RuntimeError(
                "LoggerManager has not been initialized."
            )

        self.register_service(self._logger)
        
    def run(self) -> FastAPI:
        """
        Возвращает подготовленный экземпляр FastAPI.

        Returns
        -------
        FastAPI
            Полностью инициализированное приложение.
        """

        if not self._initialized:
            self.initialize()

        return self._api

    @asynccontextmanager
    async def _lifespan(
        self,
        app: FastAPI,
    ) -> AsyncIterator[None]:
        """
        Обработчик жизненного цикла FastAPI.
        """

        del app

        if not self._initialized:
            self.initialize()

        assert self._logger is not None

        log = self._logger.get_logger(__name__)

        log.info("Application started.")

        try:
            yield
        except Exception:
            log.exception(
                "Fatal error during application lifetime."
            )
            raise
        finally:
            self.shutdown()

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """

        return (
            f"{self.__class__.__name__}("
            f"initialized={self._initialized}, "
            f"services={len(self._services)})"
        )


__all__ = [
    "Application",
]