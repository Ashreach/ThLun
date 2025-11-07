"""
Progress bar implementation for ThLun library.
"""

import sys


class ProgressBar:
    """A customizable progress bar for terminal output."""

    def __init__(self, total: int, width: int = 50, char: str = '#'):
        """Initialize progress bar.
        
        Args:
            total: Total number of items to process.
            width: Width of the progress bar in characters.
            char: Character to use for filled portions.
        """
        self.total = total
        self.width = width
        self.char = char
        self.current = 0

    def update(self, current: int) -> None:
        """Update progress to specific value."""
        self.current = min(current, self.total)
        self._render()

    def increment(self, step: int = 1) -> None:
        """Increment progress by step amount."""
        self.current = min(self.current + step, self.total)
        self._render()

    def finish(self) -> None:
        """Complete the progress bar and add newline."""
        self.current = self.total
        self._render()
        sys.stdout.write('\033[?25h\n')
        sys.stdout.flush()

    def _render(self) -> None:
        """Render the progress bar to stdout."""
        percent = (self.current / self.total) * 100
        filled = int((self.current / self.total) * self.width)
        bar = self.char * filled + ' ' * (self.width - filled)
        sys.stdout.write(f'\r[{bar}] {percent:.0f}%\033[?25l')
        sys.stdout.flush()
