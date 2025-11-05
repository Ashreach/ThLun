"""
Input/Output operations for ThLun library.

This module provides cross-platform utilities for single-character input,
masked (secret) input, and type-restricted character scanning.
"""

import sys
import contextlib


@contextlib.contextmanager
def _raw_mode(fd: int):
    """Temporarily set terminal to raw mode (Unix only)."""
    import termios
    import tty 

    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        yield
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class IO:
    """Provides portable low-level input operations."""

    def scan(self, prompt: str = "", is_printing: bool = False, end_line: bool = True) -> str:
        """Read a single character from input without waiting for Enter.

        Args:
            prompt: Text to display before reading.
            is_printing: Whether to print the captured character.
            end_line: Whether to print a newline after printing the character.

        Returns:
            The captured character as a string.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()

        result = ""

        if sys.platform.startswith("win"):
            import msvcrt

            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):  # Skip special keys
                _ = msvcrt.getwch()
                return ""
            result = ch
        else:
            fd = sys.stdin.fileno()
            with _raw_mode(fd):
                result = sys.stdin.read(1)

        if is_printing:
            sys.stdout.write(result)
            if end_line:
                sys.stdout.write("\n")
            sys.stdout.flush()

        return result

    def scan_with_types(
        self,
        prompt: str = "",
        allowed_types: list[str] | None = None,
        is_printing: bool = False,
    ) -> str:
        """Read one character filtered by allowed type groups.

        Args:
            prompt: Prompt to display.
            allowed_types: List of allowed categories: ``["chars"]``, ``["numbers"]`` or both.
            is_printing: Whether to print accepted character immediately.

        Returns:
            First valid character.
        """
        if allowed_types is None:
            allowed_types = ["chars", "numbers"]

        allowed_chars: set[str] = set()

        if "chars" in allowed_types:
            allowed_chars.update(
                [chr(c) for c in range(ord("a"), ord("z") + 1)]
                + [chr(c) for c in range(ord("A"), ord("Z") + 1)]
            )
        if "numbers" in allowed_types:
            allowed_chars.update(chr(c) for c in range(ord("0"), ord("9") + 1))

        while True:
            char = self.scan(prompt, is_printing=False)
            if char in allowed_chars:
                if is_printing:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                return char

    def secret(self, prompt: str = "", spoiler: str = "*", end_line: bool = True) -> str:
        """Read a masked (secret) string from input.

        Each character is hidden with a given spoiler symbol (e.g., '*').

        Args:
            prompt: Prompt text.
            spoiler: Character used to mask input.
            end_line: Whether to print newline after completion.

        Returns:
            Entered secret string.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()

        secret = ""

        while True:
            char = self.scan(end_line=False)

            if char in ("\r", "\n"):  # Enter pressed
                break
            elif char in ("\x08", "\x7f"):  # Backspace
                if secret:
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                    secret = secret[:-1]
            else:
                sys.stdout.write(spoiler)
                sys.stdout.flush()
                secret += char

        if end_line:
            sys.stdout.write("\n")

        return secret
