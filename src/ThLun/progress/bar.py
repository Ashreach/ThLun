"""
Progress bar implementation for ThLun library.
"""

import sys
import time
from ..io import RESET, Colors, fg


class ProgressBar:
    """A progress bar for terminal."""
    _instances = []
    _line_count = 0

    def __init__(self, total: int, width: int = 50, char: str = '#', color = None, empty: str = ' '):
        """Initialize progress bar.
        
        Args:
            total: Total number of items to process.
            width: Width of the progress bar in characters.
            char: Character to use for filled portions.
            color: Color name (e.g. 'GREEN'), number (0-255), or ANSI code.
            empty: Character to use for empty portions.
        """
        self.total = total
        self.width = width
        self.char = char
        self.empty = empty
        self.color = self._parse_color(color)
        self.current = 0
        self.start_time = time.time()
        
        ProgressBar._instances.append(self)
        self.line_index = len(ProgressBar._instances) - 1

        sys.stdout.write('\n')
        sys.stdout.flush()
        ProgressBar._line_count = len(ProgressBar._instances)

    def _parse_color(self, color) -> str:
        """Parse color input to ANSI code."""
        if color is None:
            return ''
        if isinstance(color, str):
            if hasattr(Colors, color.upper()):
                return fg(getattr(Colors, color.upper()))
            return color
        if isinstance(color, int):
            return fg(color)
        return str(color)

    def update(self, current: int) -> None:
        """Update progress to specific value."""
        self.current = min(current, self.total)
        self._render()
        if self.current == self.total:
            self.finish()

    def increment(self, step: int = 1) -> None:
        """Increment progress by step amount."""
        self.current = min(self.current + step, self.total)
        self._render()
        if self.current == self.total:
            self.finish()

    def finish(self) -> None:
        """Complete the progress bar and add newline."""
        self.current = self.total
        self._render()
        
        # Check if all progress bars are finished
        all_finished = all(bar.current == bar.total for bar in ProgressBar._instances)
        if all_finished:
            sys.stdout.write('\n')
        
        # Show cursor
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    def _render(self) -> None:
        """Render the progress bar to stdout."""
        elapsed = time.time() - self.start_time
        minutes, seconds = divmod(int(elapsed), 60)
        time_str = f"[{minutes:02d}:{seconds:02d}]"
        
        percent = (self.current / self.total) * 100
        filled = int((self.current / self.total) * self.width)
        filled_bar = self.color + self.char * filled + RESET
        empty_bar = self.empty * (self.width - filled)
        bar = filled_bar + empty_bar
        
        # Move cursor to this bar's line from bottom
        lines_up = ProgressBar._line_count - self.line_index - 1
        if lines_up > 0:
            sys.stdout.write(f'\033[{lines_up}A')
        
        sys.stdout.write(f'\r{time_str} [{bar}] {percent:.0f}%\033[?25l')
        
        # Move cursor back to bottom
        if lines_up > 0:
            sys.stdout.write(f'\033[{lines_up}B')
        
        sys.stdout.flush()
