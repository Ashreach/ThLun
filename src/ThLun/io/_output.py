"""
Output operations for ThLun library.
Supports:
    - Named placeholders like [RED], [BACK_BLUE], [BOLD], [RESET]
    - Numeric color codes:
        [31]   → foreground
        [BG44] → background
"""

from .ansi import RESET, Back, Fore, Style, fg_replacer, bg_replacer
import re


class OUTPUT:
    """Formatted console output with ANSI placeholder and numeric color support."""

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

        for name, value in vars(Fore).items():
            if not name.startswith("_"):
                placeholders[name.upper()] = value

        for name, value in vars(Back).items():
            if not name.startswith("_"):
                placeholders[f"BG_{name.upper()}"] = value

        for name, value in vars(Style).items():
            if not name.startswith("_"):
                placeholders[name.upper()] = value

        placeholders["RESET"] = RESET

        cls._placeholders = placeholders
        return placeholders

    @classmethod
    def _replace_numeric_colors(cls, text: str) -> str:
        """
        Replace numeric and BGn placeholders using fg/bg functions:
            [31]   -> fg(31)
            [BG44] -> bg(44)
        """

        # Background color [BG44]
        text = re.sub(r"\[BG(\d{1,3})\]", lambda m: bg_replacer(int(m.group(1))), text)

        # Foreground color [31]
        text = re.sub(r"\[(\d{1,3})\]", lambda m: fg_replacer(int(m.group(1))), text)

        return text

    @classmethod
    def bprint(cls, *args, **kwargs):
        """
        Print with placeholders and numeric color support.

        Examples:
            OUTPUT.bprint("[RED][BOLD]Error:[RESET] Something went wrong!")
            OUTPUT.bprint("[31]text[RESET]")
            OUTPUT.bprint("[BG46][30]test[RESET]")
        """
        text = "".join(map(str, args))
        placeholders = cls._get_placeholders()

        for placeholder, value in placeholders.items():
            text = text.replace(f"[{placeholder}]", value)

        text = cls._replace_numeric_colors(text)

        cls._print(text, **kwargs)


bprint = OUTPUT.bprint
