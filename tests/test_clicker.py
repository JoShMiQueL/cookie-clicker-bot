"""Tests for autoclicker module."""

import threading
import time
from unittest.mock import MagicMock

import pytest

from src import config
from src.clicker import AutoClicker


class TestAutoClicker:
    """Test autoclicker functionality."""

    @pytest.fixture
    def stop_event(self):
        """Create a stop event."""
        return threading.Event()

    @pytest.fixture
    def mock_hwnd(self):
        """Mock window handle."""
        return 12345

    @pytest.fixture
    def clicker(self, mock_hwnd, stop_event, monkeypatch):
        """Create an AutoClicker instance with mocked dependencies."""
        import win32gui

        monkeypatch.setattr(win32gui, "GetClientRect", lambda hwnd: (0, 0, 1000, 800))
        monkeypatch.setattr(
            win32gui, "ClientToScreen", lambda hwnd, coords: (coords[0] + 100, coords[1] + 100)
        )

        return AutoClicker(mock_hwnd, stop_event)

    def test_initialization(self, clicker, mock_hwnd):
        """Test that AutoClicker initializes correctly."""
        assert clicker.hwnd == mock_hwnd
        assert clicker.click_delay == 1.0 / config.CPS
        assert isinstance(clicker.click_x, int)
        assert isinstance(clicker.click_y, int)

    def test_calculate_cookie_position(self, clicker):
        """Test cookie position calculation."""
        # With client rect (0, 0, 1000, 800)
        expected_x = int(1000 * config.BIG_COOKIE_RELATIVE_X)
        expected_y = int(800 * config.BIG_COOKIE_RELATIVE_Y)

        assert clicker.click_x == expected_x
        assert clicker.click_y == expected_y

    def test_update_position(self, clicker, monkeypatch):
        """Test position update."""
        import win32gui

        # Change the client rect
        monkeypatch.setattr(win32gui, "GetClientRect", lambda hwnd: (0, 0, 2000, 1600))

        original_x = clicker.click_x
        original_y = clicker.click_y

        clicker.update_position()

        # Position should change with new window size
        assert clicker.click_x != original_x or clicker.click_y != original_y

    def test_update_cps(self, clicker):
        """Test CPS update."""
        original_delay = clicker.click_delay

        # Change CPS
        config.CPS = 30
        clicker.update_cps()

        assert clicker.click_delay == 1.0 / 30
        assert clicker.click_delay != original_delay

        # Restore original CPS
        config.CPS = 15

    def test_get_screen_position(self, clicker, monkeypatch):
        """Test getting screen position."""
        import win32gui

        expected_screen_pos = (500, 400)
        monkeypatch.setattr(win32gui, "ClientToScreen", lambda hwnd, coords: expected_screen_pos)

        screen_pos = clicker.get_screen_position()
        assert screen_pos == expected_screen_pos

    def test_send_click(self, clicker, monkeypatch):
        """Test sending a click."""
        import win32api
        import win32con

        mock_send_message = MagicMock()
        monkeypatch.setattr(win32api, "SendMessage", mock_send_message)

        clicker.send_click()

        # Should send both button down and button up messages
        assert mock_send_message.call_count == 2

        # Verify the messages sent
        calls = mock_send_message.call_args_list
        assert calls[0][0][1] == win32con.WM_LBUTTONDOWN
        assert calls[1][0][1] == win32con.WM_LBUTTONUP

    def test_run_stops_on_event(self, clicker, stop_event, monkeypatch):
        """Test that run loop stops when event is set."""
        import win32api

        click_count = 0

        def mock_send_message(*args):
            nonlocal click_count
            click_count += 1

        monkeypatch.setattr(win32api, "SendMessage", mock_send_message)

        # Set stop event after a short delay
        def stop_after_delay():
            time.sleep(0.1)
            stop_event.set()

        stop_thread = threading.Thread(target=stop_after_delay, daemon=True)
        stop_thread.start()

        # Run the clicker
        clicker.run()

        # Should have sent some clicks but stopped
        assert click_count > 0
        assert stop_event.is_set()

    def test_click_delay_accuracy(self, clicker):
        """Test that click delay is calculated correctly."""
        test_cps_values = [1, 5, 10, 15, 20, 30, 50]

        for cps in test_cps_values:
            config.CPS = cps
            clicker.update_cps()
            expected_delay = 1.0 / cps
            assert abs(clicker.click_delay - expected_delay) < 0.0001

        # Restore original CPS
        config.CPS = 15

    def test_l_param_calculation(self, clicker, monkeypatch):
        """Test that l_param is calculated correctly for click position."""
        import win32api

        captured_l_param = None

        def mock_send_message(hwnd, msg, w_param, l_param):
            nonlocal captured_l_param
            captured_l_param = l_param

        monkeypatch.setattr(win32api, "SendMessage", mock_send_message)

        clicker.send_click()

        # l_param should be (y << 16) | x
        expected_l_param = (clicker.click_y << 16) | clicker.click_x
        assert captured_l_param == expected_l_param
