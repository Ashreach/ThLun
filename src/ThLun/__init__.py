"""
ThLun - A Python library for generating stylish terminal output.

This library includes a cross-platform way to read single characters from
input, and a 256-color ANSI wrapper for terminal printing.
"""

from .core import Console
from .ansi import Fore, Back, RESET, clear_screen, clear_line, Cursor
from .io import IO

__all__ = ["Console", "IO", "Fore", "Back", "RESET", "clear_screen", "clear_line", "Cursor"]
__version__ = "0.1.0"
