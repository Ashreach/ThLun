"""
Output operations for ThLun library.
Supports ANSI placeholders like [RED], [BACK_BLUE], [BOLD], [RESET].
"""

from . import RESET, Back256, Fore256, Style


class OUTPUT:
    """Formatted console output with automatic ANSI color replacement."""

    _placeholders = None

    @staticmethod
    def _print(*args, **kwargs):
        """Wrapper around print() with flush always enabled."""
        print(*args, **kwargs, flush=True)

    @classmethod
    def _get_placeholders(cls):
        """Collect and cache all placeholders from color/style classes."""
        if cls._placeholders is not None:
            return cls._placeholders

        placeholders = {}

        for name, value in vars(Fore256).items():
            if not name.startswith("_"):
                placeholders[name.upper()] = value

        for name, value in vars(Back256).items():
            if not name.startswith("_"):
                placeholders[f"BACK_{name.upper()}"] = value

        for name, value in vars(Style).items():
            if not name.startswith("_"):
                placeholders[name.upper()] = value

        placeholders["RESET"] = RESET

        cls._placeholders = placeholders
        return placeholders

    @classmethod
    def bprint(cls, *args, **kwargs):
        """
        Print with placeholders.
        Example:
            OUTPUT.bprint("[RED][BOLD]Error:[RESET] Something went wrong!\n")
        """
        text = "".join(map(str, args))
        placeholders = cls._get_placeholders()

        for placeholder, value in placeholders.items():
            text = text.replace(f"[{placeholder}]", value)

        cls._print(text, **kwargs)
