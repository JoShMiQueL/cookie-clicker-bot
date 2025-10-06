"""Module for finding and managing Cookie Clicker windows."""

import re

import win32gui


class CookieClickerWindowFinder:
    """Responsible for finding the Cookie Clicker window."""

    @staticmethod
    def is_cookie_clicker_window(title: str) -> bool:
        """Verify if the title matches the dynamic Cookie Clicker pattern."""
        # Pattern: "[number with possible commas] cookies - Cookie Clicker"
        # Examples: "245 cookies", "1,111 cookies", "19,631 cookies"
        pattern = r"^[\d,]+\s*cookies\s*-\s*Cookie Clicker$"
        return bool(re.match(pattern, title, re.IGNORECASE))

    def find_window(self) -> int | None:
        """Find the Cookie Clicker window with dynamic title."""

        def enum_window_callback(hwnd, window_list):
            if win32gui.IsWindowVisible(hwnd):
                window_title = win32gui.GetWindowText(hwnd)
                if self.is_cookie_clicker_window(window_title):
                    window_list.append((hwnd, window_title))

        windows = []
        win32gui.EnumWindows(enum_window_callback, windows)

        if not windows:
            print("❌ No window found with pattern 'X cookies - Cookie Clicker'")
            self._print_diagnostic_info()
            return None

        # Return the first match
        hwnd, title = windows[0]
        print(f"🎮 Game detected: '{title}' (HWND: {hwnd})")
        return hwnd

    def _print_diagnostic_info(self):
        """Show diagnostic information about relevant windows."""
        print("📌 Active windows that might be relevant:")

        # Search for windows containing "cookie" in the title
        relevant_windows = []
        win32gui.EnumWindows(
            lambda hwnd, hwnds: hwnds.append((hwnd, win32gui.GetWindowText(hwnd)))
            if "cookie" in win32gui.GetWindowText(hwnd).lower()
            else None,
            relevant_windows,
        )

        for _, title in relevant_windows:
            if title:
                print(f"  - '{title}'")

        # Show Steam windows just in case
        print("\n🔍 Steam windows detected:")
        steam_windows = []
        win32gui.EnumWindows(
            lambda hwnd, hwnds: hwnds.append((hwnd, win32gui.GetWindowText(hwnd)))
            if "steam" in win32gui.GetWindowText(hwnd).lower()
            else None,
            steam_windows,
        )

        for _, title in steam_windows:
            if title:
                print(f"  - '{title}'")

    @staticmethod
    def get_client_rect(hwnd: int) -> tuple[int, int, int, int]:
        """Get the client rectangle of the window."""
        return win32gui.GetClientRect(hwnd)

    @staticmethod
    def client_to_screen(hwnd: int, x: int, y: int) -> tuple[int, int]:
        """Convert client coordinates to screen coordinates."""
        return win32gui.ClientToScreen(hwnd, (x, y))
