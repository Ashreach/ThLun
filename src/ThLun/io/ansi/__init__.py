from .screen import Cursor, clear_line, clear_screen
from .styles import RESET, Back256, Fore256, Style
from .styles import bg as bg_replacer
from .styles import fg as fg_replacer

Back = Back256
Fore = Fore256

__all__ = [
    "fg_replacer",
    "bg_replacer",
    "Fore",
    "Back",
    "Fore256",
    "Back256",
    "RESET",
    "clear_screen",
    "clear_line",
    "Cursor",
]
