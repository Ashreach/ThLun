"""
Logger module for ThLun library.
Contains a class for logging messages with customizable logging levels and colors.
"""

import datetime
import inspect

from ThLun.io import RESET, Fore

from .types import LogLevel


class Logger:
    def __init__(self, log_level: LogLevel):
        """
        Initialize a Logger instance with the given log level.

        :param log_level: Log level associated with the logger. All log messages
            with a level less than or equal to this will be printed.
        """
        self.log_level = log_level

    def log(self, log_level: LogLevel | str, message: str, print_function=False):
        """
        Output a message with the given log level.

        :param log_level: Log level associated with the message.
        :param message: Log message to print.
        :param print_function: If True, prints the function name where the log was called.
        """
        if log_level <= self.log_level:
            self._output(message, log_level, print_function)

    @classmethod
    def _output(cls, message: str, log_level: LogLevel, print_function: bool):
        """
        Internal method for formatting and printing log messages.

        :param message: Log message to print.
        :param log_level: Log level associated with the message.
        :param print_function: If True, prints the function name where the log was called.
        """
        stack = inspect.stack()
        frame = next(
            (f for f in stack if "logger.py" not in f.filename),
            stack[-1],
        )
        filename = frame.filename.split("/")[-1]
        line = frame.lineno
        function = frame.function

        BASE_LINE = (
            "{time_color}{asctime} {RESET}"
            + "{color_breaks}[{log_level_color}{log_level_name}{color_breaks}] {RESET}"
            + "{file_color}{filename}{color_breaks}:{line_color}{line}{function_color}{function_line} {RESET}"
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

        print(BASE_LINE.format(**kwargs))

    @staticmethod
    def trace(message: str, print_function=False):
        """
        Output a message with a logging level of TRACE.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the trace was called.
        """
        Logger(LogLevel.TRACE).log(LogLevel.TRACE, message, print_function)

    @staticmethod
    def debug(message: str, print_function=False):
        """
        Output a message with a logging level of DEBUG.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the debug was called.
        """
        Logger(LogLevel.DEBUG).log(LogLevel.DEBUG, message, print_function)

    @staticmethod
    def info(message: str, print_function=False):
        """
        Output a message with a logging level of INFO.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the info was called.
        """
        Logger(LogLevel.INFO).log(LogLevel.INFO, message, print_function)

    @staticmethod
    def success(message: str, print_function=False):
        """
        Output a message with a logging level of SUCCESS.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the success was called.
        """
        Logger(LogLevel.SUCCESS).log(LogLevel.SUCCESS, message, print_function)

    @staticmethod
    def warning(message: str, print_function=False):
        """
        Output a message with a logging level of WARNING.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the warning was called.
        """
        Logger(LogLevel.WARNING).log(LogLevel.WARNING, message, print_function)

    @staticmethod
    def error(message: str, print_function=False):
        """
        Output a message with a logging level of ERROR.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the error was called.
        """
        Logger(LogLevel.ERROR).log(LogLevel.ERROR, message, print_function)

    @staticmethod
    def critical(message: str, print_function=False):
        """
        Output a message with a logging level of CRITICAL.

        :param message: Message to output.
        :param print_function: If True, prints the function name where the critical was called.
        """
        Logger(LogLevel.CRITICAL).log(LogLevel.CRITICAL, message, print_function)
