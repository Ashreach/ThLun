"""
Initialization module for ThLun's logger module.
Contains the Logger class and the LogLevel dataclass.
"""

from .logger import Logger, Formatter
from .types import LogLevel

__all__ = [
    "Logger",
    "Formatter",
    "LogLevel",
]
