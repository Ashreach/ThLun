"""
Unit tests for ThLun.progress_bar module.
"""

import unittest
from unittest.mock import patch

from ThLun.progress import ProgressBar

from ThLun.spinner import Spinners


class TestProgressBar(unittest.TestCase):
    """Tests for the ProgressBar class."""

    def setUp(self):
        """Reset ProgressBar instances before each test."""
        ProgressBar._instances.clear()
        ProgressBar._line_count = 0

    @patch("sys.stdout")
    def test_initialization_creates_instance(self, mock_stdout):
        """ProgressBar initializes properly with default parameters."""
        bar = ProgressBar(total=10)
        self.assertEqual(bar.total, 10)
        self.assertEqual(bar.width, 50)
        self.assertEqual(bar.char, "#")
        self.assertEqual(bar.current, 0)
        self.assertTrue(bar.show_spinner)
        self.assertEqual(len(ProgressBar._instances), 1)
        mock_stdout.write.assert_called_with("\n")

    def test_parse_color_string_and_int(self):
        """_parse_color returns ANSI code for string/int colors."""
        bar = ProgressBar(total=5)
        color_code = bar._parse_color("GREEN")
        self.assertTrue(color_code.startswith("\033[38;5;"))
        color_code_int = bar._parse_color(123)
        self.assertTrue(color_code_int.startswith("\033[38;5;"))
        raw_color = bar._parse_color("\033[31m")
        self.assertEqual(raw_color, "\033[31m")
        self.assertEqual(bar._parse_color(None), "")

    @patch("sys.stdout")
    @patch("time.time", return_value=1000)
    def test_update_and_increment_progress(self, mock_time, mock_stdout):
        """update() and increment() correctly update current progress and render."""
        bar = ProgressBar(total=10, spinner=False)
        bar.update(3)
        self.assertEqual(bar.current, 3)
        bar.increment(2)
        self.assertEqual(bar.current, 5)
        bar.increment(10)
        self.assertEqual(bar.current, 10)

    @patch("sys.stdout")
    @patch("time.time", return_value=1000)
    def test_finish_adds_newline_and_shows_cursor(self, mock_time, mock_stdout):
        """finish() sets current to total and prints newline if all done."""
        bar1 = ProgressBar(total=2, spinner=False)
        bar2 = ProgressBar(total=2, spinner=False)
        bar1.finish()
        self.assertEqual(bar1.current, 2)
        bar2.finish()
        output = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn("\n", output)
        self.assertIn("\033[?25h", output)

    @patch("sys.stdout")
    @patch("time.time", return_value=1000)
    def test_render_shows_percent_and_bar(self, mock_time, mock_stdout):
        """_render() outputs a bar string including percent and filled/empty characters."""
        bar = ProgressBar(total=4, width=4, spinner=False)
        bar.current = 2
        bar._render()
        output = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn("50%", output)
        self.assertIn(bar.char * 2, output)
        self.assertIn(bar.empty * 2, output)

    @patch("sys.stdout")
    @patch("time.time", return_value=1000)
    def test_spinner_cycles_through_chars(self, mock_time, mock_stdout):
        """Spinner cycles through spinner characters when enabled."""
        bar = ProgressBar(total=2, spinner=True, spinner_type=Spinners.dots)
        first_char = bar.spinner_chars[0]
        bar._render()
        output1 = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn(first_char, output1)
        bar._render()
        second_char = bar.spinner_chars[1 % len(bar.spinner_chars)]
        output2 = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn(second_char, output2)


if __name__ == "__main__":
    unittest.main()
