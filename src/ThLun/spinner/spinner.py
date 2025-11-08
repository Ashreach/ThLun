"""
This module provides a lightweight threaded spinner animation for
command-line applications. It supports live updates to spinner
frames, speed, message text, and cursor visibility.
"""

import sys
import time
from threading import Event, Lock, Thread

from .spinners import SpinnerChars


class Spinner:
    """A terminal spinner animation manager.

    Provides a threaded spinner animation for CLI feedback with support for
    dynamic updates (spinner style, message, speed, cursor state).
    """

    def __init__(
        self, spinner: SpinnerChars, speed: float = 0.05, hide_cursor: bool = True
    ):
        """Initialize the spinner instance.

        Args:
            spinner (SpinnerChars): The spinner animation definition.
            speed (float, optional): Frame delay in seconds. Defaults to 0.05.
            hide_cursor (bool, optional): Whether to hide the cursor during animation.
        """
        self._spinner = spinner
        self.speed = speed
        self._hide_cursor_default = hide_cursor
        self._hide_cursor_active = hide_cursor
        self._stop_event = Event()
        self._thread = None
        self._message = ""
        self._lock = Lock()

    def _cursor_hide(self):
        """Hide the terminal cursor."""
        if self._hide_cursor_active:
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    def _cursor_show(self):
        """Show the terminal cursor."""
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

    def _animate(self):
        """Internal animation loop (runs in a separate thread)."""
        index = 0
        self._hide_cursor_active = self._hide_cursor_default or not self._message
        self._cursor_hide()

        while not self._stop_event.is_set():
            with self._lock:
                spinner = self._spinner
                msg = self._message
                frame = spinner.chars[index % len(spinner.chars)]
                frame_len = max(len(f) for f in spinner.chars)
                speed = self.speed

            sys.stdout.write(
                f"\r\033[K{frame.ljust(frame_len)} {msg}"
                if msg
                else f"\r\033[K{frame.ljust(frame_len)}"
            )
            sys.stdout.flush()
            index += 1
            time.sleep(speed)

        self._cursor_show()

    def start(self, message: str | None = None):
        """
        Start the spinner animation.

        Args:
            message (str | None, optional): Message to display next to the spinner.
                If `None`, only the spinner will be shown.
        """
        self._message = message or ""
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = Thread(target=self._animate, daemon=True)
        self._thread.start()

    def update(
        self,
        message: str | None = None,
        spinner: SpinnerChars | None = None,
        speed: float | None = None,
        hide_cursor: bool | None = None,
    ):
        """
        Update spinner parameters dynamically.

        Args:
            message (str | None, optional): New message to display.
            spinner (SpinnerChars | None, optional): New spinner animation definition.
            speed (float | None, optional): New frame delay.
            hide_cursor (bool | None, optional): Override cursor visibility.
        """
        with self._lock:
            if message is not None:
                self._message = message
            if spinner is not None:
                self._spinner = spinner
            if speed is not None:
                self.speed = speed
            if hide_cursor is not None:
                self._hide_cursor_default = hide_cursor

    def stop(self, message: str = "✓ Done"):
        """
        Stop the spinner and display a final message.

        Args:
            message (str, optional): Final message printed after spinner stops.
                Defaults to `"✓ Done"`.
        """
        self._stop_event.set()
        if self._thread:
            self._thread.join()
        sys.stdout.write(f"\r\033[K{message}\n")
        sys.stdout.flush()
        self._cursor_show()
