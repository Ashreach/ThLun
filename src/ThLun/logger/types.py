"""
Type definitions for the Logger module of the ThLun library.
"""

from dataclasses import dataclass, field
from functools import total_ordering

from ThLun.io import Fore


@total_ordering
@dataclass(frozen=True, slots=True)
class LogLevelData:
    """Represents a logging level with name, color, and hierarchical height."""

    name: str = field(init=True)
    color: str = field(init=True)
    height: int = field(init=True)

    def __post_init__(self):
        """
        Center the level name to 10 characters.

        This ensures consistent formatting of log level names in the output.
        """
        name = self.name.center(10, " ")
        object.__setattr__(self, "name", name)

    def __eq__(self, other: object) -> bool:
        """
        Compare equality based on the height attribute.

        Args:
            other (object): Object to compare.

        Returns:
            bool: True if both levels have equal height, otherwise False.
        """
        if not isinstance(other, LogLevelData):
            return NotImplemented
        return self.height == other.height

    def __lt__(self, other: object) -> bool:
        """
        Compare ordering based on the height attribute.

        Args:
            other (object): Object to compare.

        Returns:
            bool: True if the current level's height is less than the other.
        """
        if not isinstance(other, LogLevelData):
            return NotImplemented
        return self.height < other.height


class LogLevel:
    """Defines standard logging levels with associated color and hierarchy."""

    TRACE = LogLevelData(name="TRACE", color=Fore.CYAN1, height=5)
    DEBUG = LogLevelData(name="DEBUG", color=Fore.GREEN, height=10)
    INFO = LogLevelData(name="INFO", color=Fore.STEEL_BLUE1_A, height=15)
    SUCCESS = LogLevelData(name="SUCCESS", color=Fore.LIGHT_GREEN_A, height=20)
    WARNING = LogLevelData(name="WARN", color=Fore.YELLOW, height=25)
    ERROR = LogLevelData(name="ERROR", color=Fore.RED, height=30)
    CRITICAL = LogLevelData(name="CRITICAL", color=Fore.DEEP_PINK4_C, height=35)
