"""
Unit tests for ThLun.logger module (new logging-based version).
"""

import logging
import unittest
from unittest.mock import patch

from ThLun.io import RESET, Fore
from ThLun.logger import Formatter, Logger
from ThLun.logger.types import LogLevel, LogLevelData


# ==============================================================
# LogLevelData tests
# ==============================================================
class TestLogLevelData(unittest.TestCase):
    """Tests for the LogLevelData dataclass."""

    def test_name_is_centered(self):
        level = LogLevelData(name="TEST", color=Fore.RED, height=1)
        self.assertEqual(len(level.name), 10)
        self.assertEqual(level.name.strip(), "TEST")

    def test_comparison_operators(self):
        lvl1 = LogLevelData("A", Fore.RED, 10)
        lvl2 = LogLevelData("B", Fore.GREEN, 20)
        lvl3 = LogLevelData("C", Fore.BLUE, 10)

        self.assertTrue(lvl1 < lvl2)
        self.assertTrue(lvl2 > lvl1)
        self.assertTrue(lvl1 == lvl3)
        self.assertNotEqual(lvl1, lvl2)
        with self.assertRaises(TypeError):
            _ = lvl1 < "not a level"


# ==============================================================
# LogLevel constants tests
# ==============================================================
class TestLogLevel(unittest.TestCase):
    """Ensure all predefined log levels have correct attributes."""

    def test_standard_levels(self):
        self.assertEqual(LogLevel.DEBUG.height, 20)
        self.assertEqual(LogLevel.INFO.height, 30)
        self.assertEqual(LogLevel.SUCCESS.height, 35)
        self.assertEqual(LogLevel.WARNING.height, 40)
        self.assertEqual(LogLevel.ERROR.height, 50)
        self.assertEqual(LogLevel.CRITICAL.height, 60)


# ==============================================================
# Formatter tests
# ==============================================================
class TestFormatter(unittest.TestCase):
    """Tests for ThLun custom color formatter."""

    def test_format_contains_expected_parts(self):
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=42,
            msg="Hello World",
            args=(),
            exc_info=None,
        )
        formatted = Formatter().format(record)
        self.assertIn("Hello World", formatted)
        self.assertIn("INFO", formatted)
        self.assertIn(Fore.LIGHT_SLATE_BLUE, formatted)
        self.assertIn(Fore.WHITE, formatted)
        self.assertIn(RESET, formatted)


# ==============================================================
# Logger wrapper tests
# ==============================================================
class TestLogger(unittest.TestCase):
    """Tests for ThLun Logger wrapper class."""

    def setUp(self):
        self.logger = Logger("TestLogger")

    def test_logger_has_handler(self):
        root = logging.getLogger()
        self.assertTrue(any(isinstance(h.formatter, Formatter) for h in root.handlers))

    @patch("logging.Logger.log")
    def test_info_calls_standard_logging(self, mock_log):
        self.logger.info("Information message")
        mock_log.assert_called_once()
        args, kwargs = mock_log.call_args
        self.assertIn("Information message", args[1])

    @patch("logging.Logger.log")
    def test_success_level_registered(self, mock_log):
        """Ensure SUCCESS custom level works properly."""
        self.logger.success("Success message")
        mock_log.assert_called_once()
        level_name = logging.getLevelName(25)
        self.assertEqual(level_name, "SUCCESS")

    @patch("logging.Logger.log")
    def test_error_and_critical_levels(self, mock_log):
        self.logger.error("Error!")
        self.logger.critical("Critical!")
        self.assertGreaterEqual(mock_log.call_count, 2)

    def test_set_level_changes_global(self):
        Logger.set_level(LogLevel.DEBUG)
        self.assertEqual(logging.getLogger().level, LogLevel.DEBUG.height)

    @patch("logging.Logger.log")
    def test_classmethods_delegate_to_instance(self, mock_log):
        Logger.info_("Static info test")
        Logger.warning_("Static warning test")
        Logger.error_("Static error test")
        self.assertGreaterEqual(mock_log.call_count, 3)


# ==============================================================
# Run all tests
# ==============================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
