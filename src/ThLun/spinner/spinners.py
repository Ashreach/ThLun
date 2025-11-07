"""
This module defines reusable spinner animations for terminal UIs.
Each spinner is represented as a `SpinnerChars` dataclass containing
its name and animation frames. The `Spinners` class provides a
collection of commonly used spinners and utility methods for listing
them.
"""

from dataclasses import dataclass
from typing import ClassVar, List


@dataclass(frozen=True, slots=True)
class SpinnerChars:
    """
    Immutable container for spinner animation frames.

    Attributes:
        name (str): Human-readable name of the spinner.
        chars (List[str]): List of animation frames used for rendering.
    """

    name: str
    chars: List[str]


class Spinners:
    """
    Collection of predefined spinner styles.

    Provides a variety of spinner definitions usable in CLI animations.
    Each spinner is defined as a `SpinnerChars` instance containing
    its name and animation sequence.
    """

    # ──────────────────────────────
    # Braille snake
    # ──────────────────────────────
    braille: ClassVar[SpinnerChars] = SpinnerChars(
        name="Braille Snake",
        chars=[
            "⠉⠉", "⠉⠙", "⠈⠹", "⠀⢹", "⠀⣸", "⢀⣰",
            "⣀⣠", "⣄⣀", "⣆⡀", "⣇⠀", "⡏⠀", "⠏⠁",
            "⠋⠉", "⠉⠙", "⠉⠹", "⠈⢹", "⠀⣹", "⢀⣸",
            "⣀⣰", "⣄⣠", "⣆⣀", "⣇⡀", "⣏⠀", "⡏⠁",
            "⠏⠉", "⠉⠙", "⠈⠹", "⠀⢹", "⠀⣸", "⢀⣰",
            "⣀⣠", "⣄⣀", "⣆⡀", "⣇⠀", "⡏⠀", "⠏⠁",
        ],
    )

    # ──────────────────────────────
    # Classic dots
    # ──────────────────────────────
    dots: ClassVar[SpinnerChars] = SpinnerChars(
        name="Dots",
        chars=["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
    )

    # ──────────────────────────────
    # Line spinner
    # ──────────────────────────────
    line: ClassVar[SpinnerChars] = SpinnerChars(
        name="Line",
        chars=["|", "/", "—", "\\"],
    )

    # ──────────────────────────────
    # Circle spinner
    # ──────────────────────────────
    circle: ClassVar[SpinnerChars] = SpinnerChars(
        name="Circle",
        chars=["◐", "◓", "◑", "◒"],
    )

    # ──────────────────────────────
    # Auto-collect all spinner definitions
    # ──────────────────────────────
    all: ClassVar[List[SpinnerChars]] = [
        value for key, value in vars().items() if isinstance(value, SpinnerChars)
    ]

    @classmethod
    def list(cls) -> List[str]:
        """
        Return the list of available spinner names.

        Returns:
            List[str]: Names of all defined spinner animations.
        """
        return [s.name for s in cls.all]
