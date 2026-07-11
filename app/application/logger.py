"""
Voxarium
Logging subsystem.

Единая подсистема логирования приложения.

Все модули проекта должны получать экземпляр логгера
исключительно через LoggerManager.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Final

from loguru import Logger
from loguru import logger


class LoggerManager:
    """
    Централизованное управление системой логирования.

    Экземпляр класса создается приложением один раз и
    передается остальным сервисам через контейнер сервисов.
    """

    DEFAULT_FORMAT: Final[str] = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
        " | "
        "<level>{level:<8}</level>"
        " | "
        "<cyan>{extra[module]}</cyan>"
        " | "
        "{message}"
    )

    def __init__(
        self,
        log_directory: Path,
        debug: bool = False,
    ) -> None:
        self._log_directory = log_directory
        self._debug = debug
        self._configured = False

    @property
    def configured(self) -> bool:
        return self._configured

    @property
    def log_directory(self) -> Path:
        return self._log_directory

    def configure(self) -> None:
        """
        Настраивает Loguru.

        Повторный вызов безопасен.
        """

        if self._configured:
            return

        self._log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.remove()

        self._configure_console()
        self._configure_file()
        self._configure_error_file()
        self._configure_standard_logging()

        self._configured = True

        self.get_logger(__name__).info(
            "Logging subsystem initialized."
        )

    def shutdown(self) -> None:
        """
        Корректно завершает работу подсистемы.
        """

        if not self._configured:
            return

        self.get_logger(__name__).info(
            "Logging subsystem stopped."
        )

        logger.remove()

        self._configured = False

    def get_logger(self, module: str) -> Logger:
        """
        Возвращает логгер для указанного модуля.
        """

        if not self._configured:
            raise RuntimeError(
                "LoggerManager is not configured."
            )

        return logger.bind(module=module)

    def _configure_console(self) -> None:
        """
        Консольный вывод.
        """

        logger.add(
            sys.stdout,
            level="DEBUG" if self._debug else "INFO",
            colorize=True,
            enqueue=True,
            backtrace=True,
            diagnose=False,
            format=self.DEFAULT_FORMAT,
        )
        
    def _configure_file(self) -> None:
        """
        Настраивает основной журнал приложения.
        """

        logger.add(
            self._log_directory / "voxarium.log",
            level="DEBUG",
            encoding="utf-8",
            enqueue=True,
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            backtrace=True,
            diagnose=False,
            format=self.DEFAULT_FORMAT,
        )

    def _configure_error_file(self) -> None:
        """
        Настраивает журнал ошибок.
        """

        logger.add(
            self._log_directory / "errors.log",
            level="ERROR",
            encoding="utf-8",
            enqueue=True,
            rotation="5 MB",
            retention="90 days",
            compression="zip",
            backtrace=True,
            diagnose=True,
            format=self.DEFAULT_FORMAT,
        )

    def _configure_standard_logging(self) -> None:
        """
        Перенаправляет стандартный logging в Loguru.

        Это позволяет библиотекам, использующим стандартный
        модуль logging, автоматически писать сообщения в
        единый журнал Voxarium.
        """

        class InterceptHandler(logging.Handler):
            """
            Перехватчик стандартного logging.
            """

            def emit(self, record: logging.LogRecord) -> None:
                try:
                    level = logger.level(record.levelname).name
                except ValueError:
                    level = record.levelno

                frame = logging.currentframe()
                depth = 2

                while frame is not None:
                    filename = frame.f_code.co_filename

                    if "logging" not in filename:
                        break

                    frame = frame.f_back
                    depth += 1

                logger.bind(
                    module=record.name,
                ).opt(
                    depth=depth,
                    exception=record.exc_info,
                ).log(
                    level,
                    record.getMessage(),
                )

        logging.root.handlers.clear()
        logging.root.setLevel(logging.NOTSET)
        logging.root.addHandler(
            InterceptHandler(),
        )

    def reload(
        self,
        *,
        debug: bool | None = None,
    ) -> None:
        """
        Полностью перенастраивает подсистему логирования.

        Parameters
        ----------
        debug:
            Новый режим отладки. Если None, используется
            текущее значение.
        """

        if debug is not None:
            self._debug = debug

        if self._configured:
            logger.remove()
            self._configured = False

        self.configure()
        
    def set_debug(self, enabled: bool) -> None:
        """
        Включает или отключает режим подробного логирования.

        Если подсистема уже настроена, изменения применяются
        немедленно посредством перезагрузки конфигурации.

        Parameters
        ----------
        enabled
            True для включения режима DEBUG.
        """

        if self._debug == enabled:
            return

        self.reload(debug=enabled)

    def install_exception_hook(self) -> None:
        """
        Устанавливает обработчик необработанных исключений.
        """

        def exception_handler(
            exc_type,
            exc_value,
            exc_traceback,
        ) -> None:
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(
                    exc_type,
                    exc_value,
                    exc_traceback,
                )
                return

            self.get_logger("UnhandledException").opt(
                exception=(
                    exc_type,
                    exc_value,
                    exc_traceback,
                )
            ).critical(
                "Unhandled application exception."
            )

        sys.excepthook = exception_handler


__all__ = [
    "LoggerManager",
]