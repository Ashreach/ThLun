"""
ThLun-style colorized logging built on top of Python's standard logging.

This module provides a colorized logger that integrates ThLun’s design
with Python’s built-in `logging` module. It supports custom levels,
colored output, and full compatibility with standard logging handlers.
"""

import datetime
import inspect
import logging
import sys
from typing import Any

from ThLun.io import RESET, Fore

from .types import LogLevel


# --------------------------------------------------------------------
# Custom color formatter
# --------------------------------------------------------------------
class Formatter(logging.Formatter):
    """Colorful ThLun-style formatter for log records.

    This formatter adds ThLun-style coloring and formatting to each log message.
    It displays time, level, filename, function name, and message content
    in a consistent and colorized layout.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record with colors and custom layout.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The fully formatted and colorized log message.
        """
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

        stack = inspect.stack()
        frame = next((f for f in stack if "logging" not in f.filename), stack[-1])
        filename = frame.filename.split("/")[-1]
        line = frame.lineno
        function = frame.function
        asctime = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-4]

        formatted = (
            f"{Fore.LIGHT_SLATE_BLUE}{asctime}{RESET}"
            f"{Fore.GREY35}[{lvl.color}{lvl.name}{Fore.GREY35}]{RESET} "
            f"{Fore.SLATE_BLUE1}{filename}{Fore.GREY35}:{Fore.MEDIUM_PURPLE1}{line}"
            f"{Fore.LIGHT_SLATE_BLUE}:{function}{RESET} "
            f"{Fore.GREY3}イ{Fore.WHITE}{record.getMessage()}{RESET}"
        )

        return formatted


# --------------------------------------------------------------------
# Main Logger wrapper
# --------------------------------------------------------------------
class Logger:
    """Drop-in enhanced logger with ThLun color formatting.

    A wrapper around Python's `logging` module providing ThLun-style colorful
    output and additional convenience methods for different log levels.

    Attributes:
        _global_level (int): Global minimum logging level applied to all loggers.
        logger (logging.Logger): Internal standard logger instance.
    """

    _global_level = logging.INFO

    def __init__(self, name: str = "ThLun", level: int | None = None):
        """Initialize the Logger instance.

        Args:
            name (str, optional): The logger name. Defaults to "ThLun".
            level (int | None, optional): Logging level override. Defaults to global level.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level or Logger._global_level)
        self._ensure_handler()

    @staticmethod
    def _ensure_handler():
        """Ensure a console handler with custom formatter exists.

        Guarantees that at least one StreamHandler with ThLun Formatter
        is attached to the root logger. If a handler exists but lacks
        a formatter, the custom Formatter is applied automatically.
        """
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


    # ----------------------------------------------------------------
    # Static setup method
    # ----------------------------------------------------------------
    @classmethod
    def set_level(cls, log_level: LogLevel):
        """Set the global minimum logging level.

        Args:
            log_level (LogLevel): The minimum log level to apply globally.
        """
        cls._global_level = log_level.height
        logging.getLogger().setLevel(log_level.height)

    # ----------------------------------------------------------------
    # Unified logging call
    # ----------------------------------------------------------------
    def _log(self, level: int, message: str, *args: Any, **kwargs: Any):
        """Log a message using the standard logging mechanism.

        Args:
            level (int): The numeric level for the log record.
            message (str): The message text to log.
            *args: Additional positional arguments passed to `logging.Logger.log`.
            **kwargs: Additional keyword arguments passed to `logging.Logger.log`.
        """
        self.logger.log(level, message, *args, **kwargs)

    # ----------------------------------------------------------------
    # Level-specific instance methods
    # ----------------------------------------------------------------
    def trace(self, message: str):
        """Log a message at TRACE level (custom)."""
        self._log(10, message)

    def debug(self, message: str):
        """Log a message at DEBUG level."""
        self._log(logging.DEBUG, message)

    def info(self, message: str):
        """Log a message at INFO level."""
        self._log(logging.INFO, message)

    def success(self, message: str):
        """Log a message at SUCCESS level (custom level between INFO and WARNING)."""
        logging.addLevelName(25, "SUCCESS")
        self._log(25, message)

    def warning(self, message: str):
        """Log a message at WARNING level."""
        self._log(logging.WARNING, message)

    def error(self, message: str):
        """Log a message at ERROR level."""
        self._log(logging.ERROR, message)

    def critical(self, message: str):
        """Log a message at CRITICAL level."""
        self._log(logging.CRITICAL, message)

    # ----------------------------------------------------------------
    # Class-level shorthands for global logging
    # ----------------------------------------------------------------
    @classmethod
    def trace_(cls, message: str):
        """Static TRACE log call using a global logger."""
        cls("ThLun").trace(message)

    @classmethod
    def debug_(cls, message: str):
        """Static DEBUG log call using a global logger."""
        cls("ThLun").debug(message)

    @classmethod
    def info_(cls, message: str):
        """Static INFO log call using a global logger."""
        cls("ThLun").info(message)

    @classmethod
    def success_(cls, message: str):
        """Static SUCCESS log call using a global logger."""
        cls("ThLun").success(message)

    @classmethod
    def warning_(cls, message: str):
        """Static WARNING log call using a global logger."""
        cls("ThLun").warning(message)

    @classmethod
    def error_(cls, message: str):
        """Static ERROR log call using a global logger."""
        cls("ThLun").error(message)

    @classmethod
    def critical_(cls, message: str):
        """Static CRITICAL log call using a global logger."""
        cls("ThLun").critical(message)
