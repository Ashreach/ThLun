"""
Screen and cursor operations for the ThLun library.

This module contains platform-agnostic functions for clearing the screen
and moving the cursor.
"""

CSI = "\033["
OSC = "\033]"
BEL = "\a"


def clear_screen(mode: int = 2) -> str:
    """
    Clear the screen.

    Args:
        mode: Clear mode.
            0 - from cursor to end of screen
            1 - from cursor to beginning
            2 - entire screen

    Returns:
        The ANSI escape sequence to clear the screen.
    """
    return CSI + str(mode) + "J"


def clear_line(mode: int = 2) -> str:
    """
    Clear the current line.

    Args:
        mode: Clear mode.
            0 - from cursor to end of line
            1 - from cursor to beginning
            2 - entire line

    Returns:
        The ANSI escape sequence to clear the line.
    """
    return CSI + str(mode) + "K"


class Cursor:
    """ANSI cursor movement utilities."""

    @staticmethod
    def up(n: int = 1) -> str:
        """Move the cursor up by n lines."""
        return CSI + str(n) + "A"

    @staticmethod
    def down(n: int = 1) -> str:
        """Move the cursor down by n lines."""
        return CSI + str(n) + "B"

    @staticmethod
    def forward(n: int = 1) -> str:
        """Move the cursor forward (right) by n columns."""
        return CSI + str(n) + "C"

    @staticmethod
    def back(n: int = 1) -> str:
        """Move the cursor back (left) by n columns."""
        return CSI + str(n) + "D"

    @staticmethod
    def pos(x: int = 1, y: int = 1) -> str:
        """Move the cursor to position (x, y)."""
        return CSI + f"{y};{x}H"
