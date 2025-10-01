import sys


class IO:
    def scan(self, text: str, is_printing: bool = False) -> str:
        """Зчитує один символ без Enter (одразу після натискання клавіші)."""
        sys.stdout.write(text)
        sys.stdout.flush()

        if sys.platform.startswith("win"):
            import msvcrt

            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):
                msvcrt.getwch()
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

        print(result if is_printing else "")

        return result

    def scan_with_types(self, text: str, available_types=["chars", "numbers"], is_printing: bool = False) -> str:
        """
        Зчитує клавішу, дозволяючи лише символи з вказаних типів.
        :param text: Текст-підказка
        :param available_types: Список дозволених типів ('chars', 'numbers')
        :param is_printing: Виводити натиснуту клавішу
        :return: Перший допустимий символ
        """
        allowed_chars = set()

        if "chars" in available_types:
            allowed_chars.update(
                [chr(c) for c in range(ord('a'), ord('z') + 1)] +
                [chr(c) for c in range(ord('A'), ord('Z') + 1)]
            )
        if "numbers" in available_types:
            allowed_chars.update([chr(c) for c in range(ord('0'), ord('9') + 1)])

        while True:
            char = self.scan(text, is_printing=False)
            if char in allowed_chars:
                if is_printing:
                    print(char)
                return char

    @staticmethod
    def print(*args, **kwargs):
        print(*args, **kwargs, flush=True)
