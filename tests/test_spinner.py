"""
Unit tests for ThLun.spinner module.
"""

import time
import unittest
from unittest.mock import patch

from ThLun.spinner import Spinner, SpinnerChars, Spinners


class TestSpinnerChars(unittest.TestCase):
    """Tests for SpinnerChars dataclass and Spinners collection."""

    def test_spinnerchars_attributes(self):
        spinner = SpinnerChars(name="Test", chars=["-", "+"])
        self.assertEqual(spinner.name, "Test")
        self.assertEqual(spinner.chars, ["-", "+"])

    def test_spinners_class_contains_known_spinners(self):
        self.assertIn("Dots", Spinners.list())
        self.assertIn("Braille Snake", Spinners.list())
        self.assertTrue(all(isinstance(s, SpinnerChars) for s in Spinners.all))


class TestSpinner(unittest.TestCase):
    """Tests for Spinner class."""

    @patch("sys.stdout")
    @patch("time.sleep", return_value=None)
    def test_start_creates_thread_and_writes_output(self, mock_sleep, mock_stdout):
        spinner = Spinner(Spinners.dots, speed=0.01)
        spinner.start("Loading")
        time.sleep(0.05)
        self.assertTrue(spinner._thread.is_alive())
        spinner.stop()
        written = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn("Loading", written)
        self.assertIn("✓ Done", written)

    @patch("sys.stdout")
    @patch("time.sleep", return_value=None)
    def test_update_changes_parameters(self, mock_sleep, mock_stdout):
        spinner = Spinner(Spinners.dots, speed=0.1)
        spinner.start("Old")
        spinner.update(
            message="New", speed=0.05, hide_cursor=False, spinner=Spinners.line
        )
        self.assertEqual(spinner._message, "New")
        self.assertEqual(spinner.speed, 0.05)
        self.assertEqual(spinner._spinner, Spinners.line)
        self.assertFalse(spinner._hide_cursor_default)
        spinner.stop()

    @patch("sys.stdout")
    @patch("time.sleep", return_value=None)
    def test_stop_sets_event_and_writes_done_message(self, mock_sleep, mock_stdout):
        spinner = Spinner(Spinners.dots)
        spinner.start()
        spinner.stop("Finished")
        self.assertTrue(spinner._stop_event.is_set())
        written = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn("Finished", written)
        self.assertIn("\033[?25h", written)

    @patch("sys.stdout")
    @patch("time.sleep", return_value=None)
    def test_spinner_animation_loop_cycles_frames(self, mock_sleep, mock_stdout):
        spinner = Spinner(Spinners.dots, speed=0.01)
        spinner.start()
        time.sleep(0.05)
        spinner.stop()
        written = "".join(call[0][0] for call in mock_stdout.write.call_args_list)
        self.assertIn(Spinners.dots.chars[0], written)


if __name__ == "__main__":
    unittest.main()
