"""
Test IO module for ThLun library.
"""

from unittest.mock import patch, MagicMock

from ThLun import IO


class TestIO:
    def test_io_creation(self):
        """Test that IO class can be instantiated"""
        io = IO()
        assert io is not None

    def test_print_method(self):
        """Test static print method"""
        with patch("builtins.print") as mock_print:
            IO.print("test message")
            mock_print.assert_called_once_with("test message", flush=True)

    @patch("sys.platform", "linux")
    @patch("sys.stdin")
    @patch("termios.tcgetattr")
    @patch("termios.tcsetattr")
    @patch("tty.setraw")
    def test_scan_unix(self, mock_setraw, mock_tcsetattr, mock_tcgetattr, mock_stdin):
        """Test scan method on Unix systems"""
        mock_stdin.fileno.return_value = 0
        mock_stdin.read.return_value = "a"
        mock_tcgetattr.return_value = MagicMock()

        io = IO()
        result = io.scan()

        assert result == "a"
    def test_scan_with_types_valid_char(self):
        """Test scan_with_types with valid character"""
        io = IO()
        with patch.object(io, "scan", return_value="a"):
            result = io.scan_with_types(allowed_types=["chars"])
            assert result == "a"
    def test_scan_with_types_valid_number(self):
        """Test scan_with_types with valid number"""
        io = IO()
        with patch.object(io, "scan", return_value="5"):
            result = io.scan_with_types(allowed_types=["numbers"])
            assert result == "5"
