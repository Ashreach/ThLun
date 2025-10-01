import sys


class Console:
    def __init__(self):
        pass

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
            import tty
            import termios

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                result = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        print(result if is_printing else "")

        return result

    @staticmethod
    def print(*args, **kwargs):
        print(*args, **kwargs, flush=True)
