"""
ThLun-style colorized logging built on top of Python's standard logging.

This module provides a colorized logger that integrates ThLun’s design
with Python’s built-in `logging` module. It supports custom levels,
colored output, and full compatibility with standard logging handlers.
"""

import datetime
import logging
import sys
import os
from typing import Any

from ThLun.io import RESET, Fore

from .types import LogLevel


class Formatter(logging.Formatter):
    """
    Colorful ThLun-style formatter for log records.

    Adds ThLun-style coloring and formatting to each log message.
    Displays time, level, filename, function name, and message content
    in a consistent and colorized layout.
    """

    def format(self, record: logging.LogRecord) -> str:
        level_map = {
            "TRACE": LogLevel.TRACE,
            "DEBUG": LogLevel.DEBUG,
            "INFO": LogLevel.INFO,
            "SUCCESS": LogLevel.SUCCESS,
            "WARNING": LogLevel.WARNING,
            "ERROR": LogLevel.ERROR,
            "CRITICAL": LogLevel.CRITICAL,
        }
        lvl = level_map.get(record.levelname, LogLevel.INFO)

        # Використовуємо дані LogRecord для точного місця виклику
        filename = os.path.basename(record.pathname)
        line = record.lineno
        function = record.funcName
        asctime = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-4]

        formatted = (
            f"{Fore.LIGHT_SLATE_BLUE}{asctime} {RESET}"
            f"{Fore.GREY35}[{lvl.color}{lvl.name}{Fore.GREY35}]{RESET} "
            f"{Fore.SLATE_BLUE1}{filename}{Fore.GREY35}:{Fore.MEDIUM_PURPLE1}{line}"
            f"{Fore.LIGHT_SLATE_BLUE}:{function}{RESET} "
            f"{Fore.GREY3}イ{Fore.WHITE}{record.getMessage()}{RESET}"
        )
        return formatted


class Logger:
    """
    Drop-in enhanced logger with ThLun color formatting.

    A wrapper around Python's `logging` module providing ThLun-style colorful
    output and additional convenience methods for different log levels.

    Attributes:
        _global_level (int): Global minimum logging level applied to all loggers.
        logger (logging.Logger): Internal standard logger instance.
    """

    _global_level = logging.INFO

    def __init__(self, level: int | LogLevel | None = None, name: str | None = None):
        """
        Initialize the Logger instance.

        Args:
            name (str | None, optional): Logger name. Defaults to "ThLun" if not provided.
            level (int | LogLevel | None, optional): Logging level override.
        """
        if name is None:
            name = "ThLun"
        self.logger = logging.getLogger(name)

        if isinstance(level, LogLevel):
            lvl = level.height
        elif isinstance(level, int):
            lvl = level
        else:
            lvl = Logger._global_level

        self.logger.setLevel(lvl)
        self._ensure_handler()


    @staticmethod
    def _ensure_handler():
        """Ensure a console handler with ThLun Formatter exists."""
        root = logging.getLogger()
        handler_exists = False
        for h in root.handlers:
            handler_exists = True
            if not isinstance(h.formatter, Formatter):
                h.setFormatter(Formatter())
        if not handler_exists:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(Formatter())
            root.addHandler(handler)
        root.setLevel(Logger._global_level)

    @classmethod
    def set_level(cls, log_level: LogLevel):
        """
        Set the global minimum logging level.

        Args:
            log_level (LogLevel): Minimum log level applied globally.
        """
        cls._global_level = log_level.height
        logging.getLogger().setLevel(log_level.height)

    def _log(self, level: int, message: str, *args: Any, **kwargs: Any):
        """Internal log call using standard logging."""
        self.logger.log(level, message, stacklevel=3, *args, **kwargs)

    # ----------------------------------------------------------------
    # Level-specific instance methods
    # ----------------------------------------------------------------
    def trace(self, message: str): self._log(10, message)
    def debug(self, message: str): self._log(logging.DEBUG, message)
    def info(self, message: str): self._log(logging.INFO, message)
    def success(self, message: str):
        logging.addLevelName(25, "SUCCESS")
        self._log(25, message)
    def warning(self, message: str): self._log(logging.WARNING, message)
    def error(self, message: str): self._log(logging.ERROR, message)
    def critical(self, message: str): self._log(logging.CRITICAL, message)
