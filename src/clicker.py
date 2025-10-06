"""Module for managing automatic clicks."""

import threading
import time

import win32api
import win32con
import win32gui

from . import config


class AutoClicker:
    """Responsible for sending automatic clicks to the game window."""

    def __init__(self, hwnd: int, stop_event: threading.Event):
        self.hwnd = hwnd
        self.stop_event = stop_event
        self.click_delay = 1.0 / config.CPS
        self.click_x, self.click_y = self._calculate_cookie_position()

    def _calculate_cookie_position(self) -> tuple[int, int]:
        """Calculate the position of the 'big cookie' using relative coordinates."""
        client_rect = win32gui.GetClientRect(self.hwnd)
        x = int(client_rect[2] * config.BIG_COOKIE_RELATIVE_X)
        y = int(client_rect[3] * config.BIG_COOKIE_RELATIVE_Y)
        return x, y

    def update_position(self):
        """Update the click position based on current configuration."""
        self.click_x, self.click_y = self._calculate_cookie_position()

    def update_cps(self):
        """Update the delay between clicks based on current configuration."""
        self.click_delay = 1.0 / config.CPS

    def get_screen_position(self) -> tuple[int, int]:
        """Get the screen coordinates of the click point."""
        return win32gui.ClientToScreen(self.hwnd, (self.click_x, self.click_y))

    def send_click(self):
        """Send a click to the cookie position."""
        # Client coordinates (relative to the window)
        l_param = (self.click_y << 16) | self.click_x

        # Use SendMessage to ensure the message is processed immediately
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, l_param)

    def run(self):
        """Execute the main autoclicker loop."""
        while not self.stop_event.is_set():
            self.send_click()
            time.sleep(self.click_delay)
