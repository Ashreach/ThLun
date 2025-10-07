"""
Initialization module for ThLun's logger module.
Contains the Logger class and the LogLevel dataclass.
"""

from .logger import Logger
from .types import LogLevel

__all__ = [
    "Logger",
    "LogLevel",
]
