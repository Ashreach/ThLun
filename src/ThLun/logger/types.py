"""
Types for the Logger module of ThLun library.
"""

from dataclasses import dataclass, field
from functools import total_ordering

from ThLun.ansi import Fore


@total_ordering
@dataclass(frozen=True, slots=True)
class LogLevelData:
    name: str = field(init=True)
    color: str = field(init=True)
    height: int = field(init=True)

    def __post_init__(self):
        """
        Centers the name of the logging level to 10 characters.

        Modifies the LogLevelData object by setting the name attribute to a centered version of the original name.
        """
        name = self.name.center(10, " ")
        object.__setattr__(self, "name", name)

    def __eq__(self, other: object) -> bool:
        """
        Compares two LogLevelData objects by their height attribute.

        :param other: object to compare
        :return: True if self.height == other.height, False otherwise
        """
        if not isinstance(other, LogLevelData):
            return NotImplemented
        return self.height == other.height

    def __lt__(self, other: object) -> bool:
        """
        Compares two LogLevelData objects by their height attribute.

        :param other: object to compare
        :return: True if self.height < other.height, False otherwise
        """
        if not isinstance(other, LogLevelData):
            return NotImplemented
        return self.height < other.height


class LogLevel:
    """Predefined logging levels with color and hierarchy height."""

    TRACE = LogLevelData(name="TRACE", color=Fore.CYAN1, height=10)
    DEBUG = LogLevelData(name="DEBUG", color=Fore.GREEN, height=20)
    INFO = LogLevelData(name="INFO", color=Fore.STEEL_BLUE1_A, height=30)
    SUCCESS = LogLevelData(name="SUCCESS", color=Fore.LIGHT_GREEN_A, height=35)
    WARNING = LogLevelData(name="WARN", color=Fore.YELLOW, height=40)
    ERROR = LogLevelData(name="ERROR", color=Fore.RED, height=50)
    CRITICAL = LogLevelData(name="CRITICAL", color=Fore.DEEP_PINK4_C, height=60)
