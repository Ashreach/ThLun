"""
Tests the ANSI escape code operations for ThLun library.
"""

import unittest
from ThLun.ansi import screen, colors


class TestANSIColors(unittest.TestCase):
    def test_fg(self):
        for code in range(0, 256):
            expected = "\033[38;5;{}m".format(code)
            self.assertEqual(colors.fg(code), expected)

    def test_bg(self):
        for code in range(0, 256):
            expected = "\033[48;5;{}m".format(code)
            self.assertEqual(colors.bg(code), expected)


class TestANSIScreen(unittest.TestCase):
    def test_clear_screen(self):
        self.assertEqual(screen.clear_screen(), "\033[2J")

    def test_clear_line(self):
        self.assertEqual(screen.clear_line(), "\033[2K")

    def test_cursor_up(self):
        self.assertEqual(screen.Cursor.UP(), "\033[1A")

    def test_cursor_down(self):
        self.assertEqual(screen.Cursor.DOWN(), "\033[1B")

    def test_cursor_forward(self):
        self.assertEqual(screen.Cursor.FORWARD(), "\033[1C")

    def test_cursor_back(self):
        self.assertEqual(screen.Cursor.BACK(), "\033[1D")

    def test_cursor_pos(self):
        self.assertEqual(screen.Cursor.POS(), "\033[1;1H")

