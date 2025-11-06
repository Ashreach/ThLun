"""
Logger module for the ThLun library.

This module defines the `Logger` class, which provides colorful, structured logging
with customizable logging levels.
"""

import datetime
import inspect

from ThLun.io import RESET, Fore
from .types import LogLevel


class Logger:
    """Customizable logger for displaying formatted messages with colors."""

    def __init__(self, log_level: LogLevel):
        """
        Initialize a Logger instance.

        Args:
            log_level (LogLevel): The minimum log level. Messages with equal or higher
                level will be printed.
        """
        self.log_level = log_level

    def log(self, log_level: LogLevel | str, message: str, print_function: bool = False):
        """
        Output a message with the given log level.

        Args:
            log_level (LogLevel | str): The log level of the message.
            message (str): The text to log.
            print_function (bool): If True, includes the function name where the log
                was called.
        """
        if log_level <= self.log_level:
            self._output(message, log_level, print_function)

    @classmethod
    def _output(cls, message: str, log_level: LogLevel, print_function: bool):
        """
        Format and print a log message.

        Args:
            message (str): The message text.
            log_level (LogLevel): The log level for this message.
            print_function (bool): Whether to show the function name in output.
        """
        stack = inspect.stack()
        frame = next(
            (f for f in stack if "logger.py" not in f.filename),
            stack[-1],
        )
        filename = frame.filename.split("/")[-1]
        line = frame.lineno
        function = frame.function

        base_line = (
            "{time_color}{asctime} {RESET}"
            + "{color_breaks}[{log_level_color}{log_level_name}{color_breaks}] {RESET}"
            + "{file_color}{filename}{color_breaks}:{line_color}{line}"
            + "{function_color}{function_line} {RESET}"
            + "{reset_color}イ{message_color}{message_text}"
        )

        kwargs = {
            "RESET": RESET,
            "time_color": Fore.LIGHT_SLATE_BLUE,
            "asctime": datetime.datetime.now().strftime("%H:%M:%S.%f")[:-4],
            "color_breaks": Fore.GREY35,
            "log_level_color": log_level.color,
            "log_level_name": log_level.name,
            "reset_color": Fore.GREY3,
            "message_color": Fore.WHITE,
            "message_text": message,
            "file_color": Fore.SLATE_BLUE1,
            "line_color": Fore.MEDIUM_PURPLE1,
            "function_color": Fore.LIGHT_SLATE_BLUE,
            "filename": filename,
            "line": line,
            "function_line": f":{function}" if print_function else "",
        }

        print(base_line.format(**kwargs))

    # Static logging methods
    @staticmethod
    def trace(message: str, print_function: bool = False):
        """
        Log a message at TRACE level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.TRACE).log(LogLevel.TRACE, message, print_function)

    @staticmethod
    def debug(message: str, print_function: bool = False):
        """
        Log a message at DEBUG level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.DEBUG).log(LogLevel.DEBUG, message, print_function)

    @staticmethod
    def info(message: str, print_function: bool = False):
        """
        Log a message at INFO level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.INFO).log(LogLevel.INFO, message, print_function)

    @staticmethod
    def success(message: str, print_function: bool = False):
        """
        Log a message at SUCCESS level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.SUCCESS).log(LogLevel.SUCCESS, message, print_function)

    @staticmethod
    def warning(message: str, print_function: bool = False):
        """
        Log a message at WARNING level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.WARNING).log(LogLevel.WARNING, message, print_function)

    @staticmethod
    def error(message: str, print_function: bool = False):
        """
        Log a message at ERROR level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.ERROR).log(LogLevel.ERROR, message, print_function)

    @staticmethod
    def critical(message: str, print_function: bool = False):
        """
        Log a message at CRITICAL level.

        Args:
            message (str): The message text.
            print_function (bool): Whether to include the calling function name.
        """
        Logger(LogLevel.CRITICAL).log(LogLevel.CRITICAL, message, print_function)
