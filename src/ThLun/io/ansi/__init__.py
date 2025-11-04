from .styles import RESET
from .styles import Back256, Fore256
from .screen import Cursor, clear_line, clear_screen

Back = Back256
Fore = Fore256

__all__ = [
    "Fore",
    "Back",
    "Fore256",
    "Back256",
    "RESET",
    "clear_screen",
    "clear_line",
    "Cursor",
]
