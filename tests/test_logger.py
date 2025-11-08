"""
Unit tests for ThLun.logger module.
"""

import datetime
import unittest
from unittest.mock import patch

from ThLun.io import RESET, Fore
from ThLun.logger import Logger
from ThLun.logger.types import LogLevel, LogLevelData


class TestLogLevelData(unittest.TestCase):
    """Tests for the LogLevelData dataclass."""

    def test_name_is_centered(self):
        """LogLevelData.name should be centered to 10 characters."""
        level = LogLevelData(name="TEST", color=Fore.RED, height=1)
        self.assertEqual(len(level.name), 10)
        self.assertEqual(level.name.strip(), "TEST")

    def test_eq_comparison(self):
        """__eq__ compares heights for equality."""
        lvl1 = LogLevelData(name="A", color=Fore.RED, height=5)
        lvl2 = LogLevelData(name="B", color=Fore.GREEN, height=5)
        lvl3 = LogLevelData(name="C", color=Fore.BLUE, height=10)

        self.assertEqual(lvl1, lvl2)
        self.assertNotEqual(lvl1, lvl3)
        self.assertFalse(lvl1 == "not a level")

    def test_lt_comparison(self):
        """__lt__ compares heights correctly."""
        lvl1 = LogLevelData(name="A", color=Fore.RED, height=5)
        lvl2 = LogLevelData(name="B", color=Fore.GREEN, height=10)
        lvl3 = LogLevelData(name="C", color=Fore.BLUE, height=5)

        self.assertTrue(lvl1 < lvl2)
        self.assertFalse(lvl2 < lvl1)
        self.assertFalse(lvl1 < lvl3)
        with self.assertRaises(TypeError):
            _ = lvl1 < "not a level"

    def test_total_ordering(self):
        """total_ordering enables all comparison operators."""
        lvl1 = LogLevelData(name="A", color=Fore.RED, height=5)
        lvl2 = LogLevelData(name="B", color=Fore.GREEN, height=10)

        self.assertTrue(lvl1 <= lvl2)
        self.assertTrue(lvl1 < lvl2)
        self.assertTrue(lvl2 >= lvl1)
        self.assertTrue(lvl2 > lvl1)


class TestLogLevel(unittest.TestCase):
    """Tests for predefined LogLevel constants."""

    def _assert_level(self, lvl, name, color, height):
        self.assertEqual(lvl.name.strip(), name)
        self.assertEqual(lvl.color, color)
        self.assertEqual(lvl.height, height)

    def test_trace_level(self):
        self._assert_level(LogLevel.TRACE, "TRACE", Fore.CYAN1, 10)

    def test_debug_level(self):
        self._assert_level(LogLevel.DEBUG, "DEBUG", Fore.GREEN, 20)

    def test_info_level(self):
        self._assert_level(LogLevel.INFO, "INFO", Fore.STEEL_BLUE1_A, 30)

    def test_success_level(self):
        self._assert_level(LogLevel.SUCCESS, "SUCCESS", Fore.LIGHT_GREEN_A, 35)

    def test_warning_level(self):
        self._assert_level(LogLevel.WARNING, "WARN", Fore.YELLOW, 40)

    def test_error_level(self):
        self._assert_level(LogLevel.ERROR, "ERROR", Fore.RED, 50)

    def test_critical_level(self):
        self._assert_level(LogLevel.CRITICAL, "CRITICAL", Fore.DEEP_PINK4_C, 60)


class TestLogger(unittest.TestCase):
    """Tests for the Logger class."""

    def setUp(self):
        self.logger = Logger(LogLevel.INFO)

    @patch("builtins.print")
    def test_log_prints_message_when_level_allows(self, mock_print):
        """log() prints message if log_level <= logger's level."""
        self.logger.log(LogLevel.INFO, "Test message")
        mock_print.assert_called_once()
        printed = mock_print.call_args[0][0]
        self.assertIn("Test message", printed)
        self.assertIn(Fore.WHITE, printed)

    @patch("builtins.print")
    def test_log_skips_message_when_level_too_high(self, mock_print):
        """log() skips message if log_level > logger's level."""
        self.logger.log(LogLevel.CRITICAL, "Hidden")
        self.assertFalse(mock_print.called)

    @patch("builtins.print")
    def test_output_formats_correctly(self, mock_print):
        """_output() formats a colorful structured log line."""
        Logger._output("Hello", LogLevel.INFO, print_function=False)
        printed = mock_print.call_args[0][0]
        self.assertIn(Fore.LIGHT_SLATE_BLUE, printed)
        self.assertIn(Fore.GREY35, printed)
        self.assertIn(Fore.WHITE, printed)
        self.assertIn("INFO", printed)
        self.assertIn("Hello", printed)
        self.assertIn(RESET, printed)

    @patch("builtins.print")
    def test_output_includes_function_name(self, mock_print):
        """_output() includes function name if print_function=True."""
        Logger._output("Func log", LogLevel.INFO, print_function=True)
        printed = mock_print.call_args[0][0]
        self.assertIn(":", printed)
        self.assertIn("Func log", printed)

    @patch("builtins.print")
    def test_static_methods_output(self, mock_print):
        """All static Logger methods print messages."""
        for method, text in [
            (Logger.trace, "trace message"),
            (Logger.debug, "debug message"),
            (Logger.info, "info message"),
            (Logger.success, "success message"),
            (Logger.warning, "warning message"),
            (Logger.error, "error message"),
            (Logger.critical, "critical message"),
        ]:
            with patch("builtins.print") as mock_print_inner:
                method(text)
                self.assertTrue(mock_print_inner.called)
                self.assertIn(text, mock_print_inner.call_args[0][0])

    @patch("builtins.print")
    def test_output_includes_timestamp(self, mock_print):
        """_output() timestamp format is correct (HH:MM:SS)."""
        now_hour = datetime.datetime.now().strftime("%H")
        Logger._output("Timing", LogLevel.INFO, print_function=False)
        printed = mock_print.call_args[0][0]
        self.assertIn(now_hour, printed)


if __name__ == "__main__":
    unittest.main()
