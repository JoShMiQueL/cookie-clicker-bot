"""Tests for GUI module."""

import threading
from unittest.mock import MagicMock, patch

from src import config


class TestAutoClickerGUI:
    """Test GUI functionality - simplified tests to avoid tkinter initialization issues."""

    def test_gui_module_imports(self):
        """Test that GUI module can be imported."""
        from src.gui import AutoClickerGUI

        assert AutoClickerGUI is not None

    @patch("src.gui.CookieClickerWindowFinder")
    @patch("tkinter.Tk")
    @patch("tkinter.IntVar")
    @patch("tkinter.DoubleVar")
    @patch("tkinter.BooleanVar")
    def test_start_clicker_window_not_found(
        self, mock_boolvar, mock_doublevar, mock_intvar, mock_tk, mock_finder_class
    ):
        """Test starting clicker when window is not found."""
        from src.gui import AutoClickerGUI

        # Configure tkinter mocks
        mock_intvar.return_value = MagicMock(get=lambda: 15)
        mock_doublevar.return_value = MagicMock(get=lambda: 0.15)
        mock_boolvar.return_value = MagicMock(get=lambda: True)

        mock_finder = MagicMock()
        mock_finder.find_window.return_value = None
        mock_finder_class.return_value = mock_finder

        with patch.object(AutoClickerGUI, "_create_widgets"):
            gui = AutoClickerGUI()
            gui.log_text = MagicMock()
            gui._start_clicker()

            assert gui.is_running is False
            mock_finder.find_window.assert_called_once()

    def test_threading_event_creation(self):
        """Test that threading events can be created."""
        event = threading.Event()
        assert not event.is_set()
        event.set()
        assert event.is_set()

    def test_config_values_accessible(self):
        """Test that config values are accessible."""
        assert hasattr(config, "CPS")
        assert hasattr(config, "BIG_COOKIE_RELATIVE_X")
        assert hasattr(config, "BIG_COOKIE_RELATIVE_Y")
        assert hasattr(config, "SHOW_OVERLAY")
