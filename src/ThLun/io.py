"""
Input/Output operations for ThLun library.
Contains platform-agnostic functions for reading single characters from input.
"""

import sys


class IO:
    def scan(self, prompt: str = "", is_printing: bool = False, end_line: bool = True) -> str:
        """
        Read a single character from input without waiting for Enter.
        Works on Windows, Linux, and macOS.

        :param prompt: Prompt to display before input.
        :param is_printing: If True, prints the captured character.
        :param end_line: If True, prints newline after character (if printed).
        :return: Captured character as str.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()

        result = ""

        if sys.platform.startswith("win"):
            import msvcrt
            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):
                _ = msvcrt.getwch()  # Skip special key second byte
                return ""
            result = ch
        else:
            import termios
            import tty

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                result = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if is_printing:
            sys.stdout.write(result)
            if end_line:
                sys.stdout.write("\n")
            sys.stdout.flush()

        return result

    def scan_with_types(
        self,
        prompt: str = "",
        allowed_types: list[str] = ["chars", "numbers"],
        is_printing: bool = False
    ) -> str:
        """
        Read one character of allowed types (letters, numbers).

        :param prompt: Prompt to display.
        :param allowed_types: List of types allowed: "chars", "numbers".
        :param is_printing: If True, prints accepted character.
        :return: First valid character.
        """
        allowed_chars = set()

        if "chars" in allowed_types:
            allowed_chars.update(
                [chr(c) for c in range(ord('a'), ord('z') + 1)] +
                [chr(c) for c in range(ord('A'), ord('Z') + 1)]
            )
        if "numbers" in allowed_types:
            allowed_chars.update([chr(c) for c in range(ord('0'), ord('9') + 1)])

        while True:
            char = self.scan(prompt, is_printing=False)
            if char in allowed_chars:
                if is_printing:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                return char

    def secret(self, prompt: str = "", spoiler: str = '*', end_line: bool = True) -> str:
        """
        Input text where each character is hidden with a spoiler symbol (e.g., '*').
        Supports backspace.

        :param prompt: Prompt to display.
        :param spoiler: Masking character.
        :param end_line: If True, prints newline after input.
        :return: The entered secret string.
        """
        sys.stdout.write(prompt)
        sys.stdout.flush()

        secret = ""

        while True:
            char = self.scan(end_line=False)

            if char in ('\r', '\n'):  # Enter
                break
            elif char in ('\x08', '\x7f'):  # Backspace (Windows / Unix)
                if secret:
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                    secret = secret[:-1]
            else:
                sys.stdout.write(spoiler)
                sys.stdout.flush()
                secret += char

        if end_line:
            print()

        return secret

    @staticmethod
    def print(*args, **kwargs):
        """
        Wrapper around built-in print() with flush always enabled.
        """
        print(*args, **kwargs, flush=True)
