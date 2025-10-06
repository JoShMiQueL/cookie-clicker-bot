"""Tests for window finder module."""

import pytest

from src.window_finder import CookieClickerWindowFinder


class TestCookieClickerWindowFinder:
    """Test window finding functionality."""

    @pytest.fixture
    def finder(self):
        """Create a window finder instance."""
        return CookieClickerWindowFinder()

    def test_is_cookie_clicker_window_simple(self, finder):
        """Test detection of simple cookie count."""
        assert finder.is_cookie_clicker_window("245 cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("1 cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("999 cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_with_commas(self, finder):
        """Test detection with comma-separated numbers."""
        assert finder.is_cookie_clicker_window("1,234 cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("1,234,567 cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_with_decimals(self, finder):
        """Test detection with decimal numbers."""
        assert finder.is_cookie_clicker_window("72.197 million cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("13.564 billion cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("6.432 trillion cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_large_numbers(self, finder):
        """Test detection with large number units."""
        assert finder.is_cookie_clicker_window("1.5 quadrillion cookies - Cookie Clicker")
        assert finder.is_cookie_clicker_window("2.3 quintillion cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_case_insensitive(self, finder):
        """Test that detection is case insensitive."""
        assert finder.is_cookie_clicker_window("245 COOKIES - Cookie Clicker")
        assert finder.is_cookie_clicker_window("1.5 MILLION cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_invalid_titles(self, finder):
        """Test rejection of invalid window titles."""
        assert not finder.is_cookie_clicker_window("Cookie Clicker")
        assert not finder.is_cookie_clicker_window("Steam")
        assert not finder.is_cookie_clicker_window("Google Chrome")
        assert not finder.is_cookie_clicker_window("")
        assert not finder.is_cookie_clicker_window("cookies - Cookie Clicker")
        assert not finder.is_cookie_clicker_window("abc cookies - Cookie Clicker")

    def test_is_cookie_clicker_window_edge_cases(self, finder):
        """Test edge cases."""
        # Extra spaces are allowed (regex is permissive for compatibility)
        assert finder.is_cookie_clicker_window("245  cookies - Cookie Clicker")
        # Missing hyphen should not match
        assert not finder.is_cookie_clicker_window("245 cookies Cookie Clicker")
        # Wrong suffix should not match
        assert not finder.is_cookie_clicker_window("245 cookies - Cookie")

    def test_get_client_rect(self, finder, monkeypatch):
        """Test getting client rectangle."""
        import win32gui

        mock_rect = (0, 0, 1920, 1080)
        monkeypatch.setattr(win32gui, "GetClientRect", lambda hwnd: mock_rect)

        rect = finder.get_client_rect(12345)
        assert rect == mock_rect

    def test_client_to_screen(self, finder, monkeypatch):
        """Test converting client to screen coordinates."""
        import win32gui

        expected_coords = (500, 400)
        monkeypatch.setattr(win32gui, "ClientToScreen", lambda hwnd, coords: expected_coords)

        coords = finder.client_to_screen(12345, 100, 200)
        assert coords == expected_coords

    def test_find_window_success(self, finder, monkeypatch):
        """Test successful window finding."""
        import win32gui

        def mock_enum_windows(callback, window_list):
            callback(12345, window_list)

        monkeypatch.setattr(win32gui, "EnumWindows", mock_enum_windows)
        monkeypatch.setattr(win32gui, "IsWindowVisible", lambda hwnd: True)
        monkeypatch.setattr(win32gui, "GetWindowText", lambda hwnd: "245 cookies - Cookie Clicker")

        hwnd = finder.find_window()
        assert hwnd == 12345

    def test_find_window_not_found(self, finder, monkeypatch, capsys):
        """Test window not found scenario."""
        import win32gui

        def mock_enum_windows(callback, window_list):
            callback(12345, window_list)

        monkeypatch.setattr(win32gui, "EnumWindows", mock_enum_windows)
        monkeypatch.setattr(win32gui, "IsWindowVisible", lambda hwnd: True)
        monkeypatch.setattr(win32gui, "GetWindowText", lambda hwnd: "Some Other Window")

        hwnd = finder.find_window()
        assert hwnd is None

        captured = capsys.readouterr()
        assert "No window found" in captured.out
