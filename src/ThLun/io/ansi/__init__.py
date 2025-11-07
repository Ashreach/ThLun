"""
ThLun terminal ansi module.

This module provides functions and classes for working with ANSI colors,
text styles, and terminal screen/cursor control.
"""

from .screen import Cursor, clear_line, clear_screen
from .styles import RESET, Back, Fore, Style, Colors, fg
from .styles import bg as bg_replacer
from .styles import fg as fg_replacer

__all__ = [
    "fg_replacer",
    "bg_replacer",
    "Colors",
    "Fore",
    "fg",
    "Back",
    "Fore",
    "Back",
    "RESET",
    "clear_screen",
    "clear_line",
    "Cursor",
    "Style"
]
