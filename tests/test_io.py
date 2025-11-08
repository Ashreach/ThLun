"""
Unit tests for ThLun.io.ansi and ThLun.io.screen modules.
"""

import unittest

from ThLun.io.ansi.styles import (
    RESET,
    Back,
    Colors,
    Fore,
    Style,
    bg_replacer,
    fg_replacer,
)
from ThLun.io.ansi.screen import (
    clear_screen,
    clear_line,
    Cursor,
    CSI,
    OSC,
    BEL,
)


class TestStyles(unittest.TestCase):
    """Tests for ANSI color and style functions."""

    def test_fg_returns_correct_format(self):
        """Check that fg_replacer() returns a valid ANSI foreground code."""
        code = 123
        result = fg_replacer(code)
        self.assertEqual(result, f"\033[38;5;{code}m")
        self.assertTrue(result.startswith("\033[38;5;"))
        self.assertTrue(result.endswith("m"))

    def test_bg_returns_correct_format(self):
        """Check that bg_replacer() returns a valid ANSI background code."""
        code = 45
        result = bg_replacer(code)
        self.assertEqual(result, f"\033[48;5;{code}m")
        self.assertTrue(result.startswith("\033[48;5;"))
        self.assertTrue(result.endswith("m"))

    def test_colors_class_constants_range(self):
        """All color constants must be integers within 0–255."""
        for name, value in vars(Colors).items():
            if not name.startswith("_"):
                self.assertIsInstance(value, int)
                self.assertTrue(0 <= value <= 255, f"{name} = {value} is out of range")

    def test_fore_and_back_have_color_constants(self):
        """Fore and Back must contain selected color constants."""
        for color_name in ["RED", "BLUE", "GREEN", "WHITE", "BLACK"]:
            fore_attr = getattr(Fore, color_name)
            back_attr = getattr(Back, color_name)
            color_code = getattr(Colors, color_name)

            self.assertEqual(fore_attr, f"\033[38;5;{color_code}m")
            self.assertEqual(back_attr, f"\033[48;5;{color_code}m")

    def test_fore_and_back_have_all_colors(self):
        """Fore and Back should define all Colors attributes."""
        color_names = [n for n in dir(Colors) if not n.startswith("_")]
        for name in color_names:
            self.assertTrue(hasattr(Fore, name))
            self.assertTrue(hasattr(Back, name))

    def test_style_constants(self):
        """Style must define standard ANSI text attributes."""
        self.assertEqual(Style.BOLD, "\033[1m")
        self.assertEqual(Style.DIM, "\033[2m")
        self.assertEqual(Style.ITALIC, "\033[3m")
        self.assertEqual(Style.UNDERLINE, "\033[4m")
        self.assertEqual(Style.REVERSE, "\033[7m")

    def test_reset_constant(self):
        """RESET should reset all ANSI formatting."""
        self.assertEqual(RESET, "\033[0m")

    def test_foreground_background_values_unique(self):
        """Foreground and background codes must differ in prefix (38 vs 48)."""
        red_fg = Fore.RED
        red_bg = Back.RED
        self.assertTrue(red_fg.startswith("\033[38;5;"))
        self.assertTrue(red_bg.startswith("\033[48;5;"))
        self.assertNotEqual(red_fg, red_bg)

    def test_fore_and_back_dynamic_generation(self):
        """Fore and Back must dynamically generate codes for all Colors."""
        for name, value in vars(Colors).items():
            if not name.startswith("_"):
                fg_val = getattr(Fore, name)
                bg_val = getattr(Back, name)
                self.assertEqual(fg_val, f"\033[38;5;{value}m")
                self.assertEqual(bg_val, f"\033[48;5;{value}m")


class TestScreen(unittest.TestCase):
    """Tests for screen and cursor utilities."""

    def test_clear_screen_returns_correct_code(self):
        """clear_screen() should return correct ANSI clear code."""
        self.assertEqual(clear_screen(), "\033[2J")
        self.assertEqual(clear_screen(0), "\033[0J")
        self.assertEqual(clear_screen(1), "\033[1J")

    def test_clear_line_returns_correct_code(self):
        """clear_line() should return correct ANSI clear-line code."""
        self.assertEqual(clear_line(), "\033[2K")
        self.assertEqual(clear_line(0), "\033[0K")
        self.assertEqual(clear_line(1), "\033[1K")

    def test_cursor_up(self):
        """Cursor.up() should move the cursor upward by n lines."""
        self.assertEqual(Cursor.up(), "\033[1A")
        self.assertEqual(Cursor.up(5), "\033[5A")

    def test_cursor_down(self):
        """Cursor.down() should move the cursor downward by n lines."""
        self.assertEqual(Cursor.down(), "\033[1B")
        self.assertEqual(Cursor.down(10), "\033[10B")

    def test_cursor_forward(self):
        """Cursor.forward() should move cursor right by n columns."""
        self.assertEqual(Cursor.forward(), "\033[1C")
        self.assertEqual(Cursor.forward(3), "\033[3C")

    def test_cursor_back(self):
        """Cursor.back() should move cursor left by n columns."""
        self.assertEqual(Cursor.back(), "\033[1D")
        self.assertEqual(Cursor.back(7), "\033[7D")

    def test_cursor_position(self):
        """Cursor.pos() should position cursor at given coordinates."""
        self.assertEqual(Cursor.pos(), "\033[1;1H")
        self.assertEqual(Cursor.pos(10, 5), "\033[5;10H")

    def test_constants_defined(self):
        """Check ANSI constant values are defined correctly."""
        self.assertEqual(CSI, "\033[")
        self.assertEqual(OSC, "\033]")
        self.assertEqual(BEL, "\a")


if __name__ == "__main__":
    unittest.main()
