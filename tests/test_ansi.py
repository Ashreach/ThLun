"""
Tests the ANSI escape code operations for ThLun library.
"""

import unittest
from src.ThLun.ansi import screen, colors

class TestScreen(unittest.TestCase):
    def test_screen_operations(self):
        """
        Tests the screen operations.

        It checks that the clear screen and clear line operations work correctly.
        """
        self._test_clear_screen()
        self._test_clear_line()

    def test_cursor_operations(self):
        """
        Tests that the cursor operations work correctly.

        It checks that the cursor can move up, down, forward, backward, and set its position.
        """
        self._test_cursor_up()
        self._test_cursor_down()
        self._test_cursor_forward()
        self._test_cursor_back()
        self._test_cursor_pos()

    def test_colors(self):
        """
        Tests the colors module.

        It checks that colors.fg() and colors.bg() return the correct ANSI escape code for all 256 colors.
        """
        self._test_colors_fg()
        self._test_colors_bg()

    def _test_clear_screen(self):
        """
        Tests that screen.clear_screen() returns the correct ANSI escape code for clearing the screen.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[2J'
        self.assertEqual(screen.clear_screen(), expected)

    def _test_clear_line(self):
        """
        Tests that screen.clear_line() returns the correct ANSI escape code for clearing the current line.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[2K'
        self.assertEqual(screen.clear_line(), expected)

    def _test_cursor_up(self):
        """
        Tests that screen.Cursor.UP() returns the correct ANSI escape code for moving the cursor up one line.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[1A'
        self.assertEqual(screen.Cursor.UP(), expected)

    def _test_cursor_down(self):
        """
        Tests that screen.Cursor.DOWN() returns the correct ANSI escape code for moving the cursor down one line.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[1B'
        self.assertEqual(screen.Cursor.DOWN(), expected)

    def _test_cursor_forward(self):
        """
        Tests that screen.Cursor.FORWARD() returns the correct ANSI escape code for moving the cursor forward one character.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[1C'
        self.assertEqual(screen.Cursor.FORWARD(), expected)

    def _test_cursor_back(self):
        """
        Tests that screen.Cursor.BACK() returns the correct ANSI escape code for moving the cursor back one character.

        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[1D'
        self.assertEqual(screen.Cursor.BACK(), expected)

    def _test_cursor_pos(self):
        """
        Tests that screen.Cursor.POS() returns the correct ANSI escape code for setting the cursor position.
        
        It checks that the returned ANSI escape code matches the expected format.
        """
        expected = '\033[1;1H'
        self.assertEqual(screen.Cursor.POS(), expected)

    def _test_colors_fg(self):
        """
        Tests that colors.fg() returns the correct ANSI escape code for all 256 colors.

        It loops over all 256 possible colors and checks that the returned ANSI escape code
        matches the expected format.
        """
        expected = '\033[38;5;{}m'
        for code in range(0, 256):
            color = colors.fg(code)
            self.assertEqual(color, expected.format(code))

    def _test_colors_bg(self):
        """
        Tests that colors.bg() returns the correct ANSI escape code for all 256 colors.
        """
        expected = '\033[48;5;{}m'
        for code in range(0, 256):
            color = colors.bg(code)
            self.assertEqual(color, expected.format(code))
