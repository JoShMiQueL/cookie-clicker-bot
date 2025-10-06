"""Tests for overlay module."""

import threading
from unittest.mock import MagicMock, patch

import pytest

from src.overlay import ClickOverlay


class TestClickOverlay:
    """Test overlay functionality."""

    @pytest.fixture
    def overlay(self):
        """Create an overlay instance."""
        return ClickOverlay()

    def test_initialization(self, overlay):
        """Test that overlay initializes correctly."""
        assert overlay.parent is None
        assert overlay.root is None
        assert overlay.canvas is None
        assert overlay.running is False
        assert isinstance(overlay.position_ready, threading.Event)
        assert overlay.click_x == 0
        assert overlay.click_y == 0

    def test_initialization_with_parent(self):
        """Test overlay initialization with parent."""
        mock_parent = MagicMock()
        overlay = ClickOverlay(parent=mock_parent)
        assert overlay.parent == mock_parent

    def test_set_position(self, overlay):
        """Test setting overlay position."""
        x, y = 500, 400
        overlay.set_position(x, y)

        assert overlay.click_x == x
        assert overlay.click_y == y
        assert overlay.position_ready.is_set()

    def test_set_position_multiple_times(self, overlay):
        """Test setting position multiple times."""
        overlay.set_position(100, 200)
        assert overlay.click_x == 100
        assert overlay.click_y == 200

        overlay.set_position(300, 400)
        assert overlay.click_x == 300
        assert overlay.click_y == 400

    @patch("tkinter.Tk")
    def test_create_overlay_without_parent(self, mock_tk, overlay):
        """Test creating overlay without parent."""
        mock_root = MagicMock()
        mock_tk.return_value = mock_root

        overlay.set_position(500, 400)
        overlay.create_overlay()

        # Should create a Tk instance
        mock_tk.assert_called_once()
        assert overlay.root == mock_root

    @patch("tkinter.Toplevel")
    def test_create_overlay_with_parent(self, mock_toplevel):
        """Test creating overlay with parent."""
        mock_parent = MagicMock()
        mock_root = MagicMock()
        mock_toplevel.return_value = mock_root

        overlay = ClickOverlay(parent=mock_parent)
        overlay.set_position(500, 400)
        overlay.create_overlay()

        # Should create a Toplevel instance
        mock_toplevel.assert_called_once_with(mock_parent)
        assert overlay.root == mock_root

    def test_create_overlay_waits_for_position(self, overlay):
        """Test that create_overlay waits for position to be set."""
        # Don't set position
        with patch("tkinter.Tk") as mock_tk:
            # Should timeout waiting for position
            overlay.create_overlay()
            # Should not create window if position not set in time
            mock_tk.assert_not_called()

    def test_update_position(self, overlay):
        """Test updating overlay position."""
        mock_root = MagicMock()
        overlay.root = mock_root
        overlay.running = True

        new_x, new_y = 600, 500
        overlay.update_position(new_x, new_y)

        assert overlay.click_x == new_x
        assert overlay.click_y == new_y
        # Should call geometry to update position
        mock_root.geometry.assert_called()

    def test_update_position_when_not_running(self, overlay):
        """Test that update_position handles non-running state."""
        overlay.running = False
        # Should not raise an error
        overlay.update_position(100, 200)

    def test_update_position_without_root(self, overlay):
        """Test that update_position handles missing root."""
        overlay.root = None
        overlay.running = True
        # Should not raise an error
        overlay.update_position(100, 200)

    def test_close(self, overlay):
        """Test closing the overlay."""
        mock_root = MagicMock()
        overlay.root = mock_root
        overlay.running = True

        overlay.close()

        assert overlay.running is False
        mock_root.destroy.assert_called_once()

    def test_close_when_not_running(self, overlay):
        """Test closing when overlay is not running."""
        mock_root = MagicMock()
        overlay.root = mock_root
        overlay.running = False

        overlay.close()

        # Should not call destroy if not running
        mock_root.destroy.assert_not_called()

    def test_close_handles_exceptions(self, overlay):
        """Test that close handles exceptions gracefully."""
        mock_root = MagicMock()
        mock_root.destroy.side_effect = Exception("Test exception")
        overlay.root = mock_root
        overlay.running = True

        # Should not raise exception
        overlay.close()
        assert overlay.running is False

    def test_overlay_geometry_calculation(self, overlay):
        """Test that overlay geometry is calculated correctly."""
        with patch("tkinter.Tk") as mock_tk:
            mock_root = MagicMock()
            mock_tk.return_value = mock_root

            x, y = 500, 400
            overlay.set_position(x, y)
            overlay.create_overlay()

            # Size should be 40x40 centered on click position
            size = 40
            expected_geometry = f"{size}x{size}+{x - size // 2}+{y - size // 2}"
            mock_root.geometry.assert_called_with(expected_geometry)

    def test_overlay_attributes(self, overlay):
        """Test that overlay has correct window attributes."""
        with patch("tkinter.Tk") as mock_tk:
            mock_root = MagicMock()
            mock_tk.return_value = mock_root

            overlay.set_position(500, 400)
            overlay.create_overlay()

            # Should set transparent color
            mock_root.attributes.assert_any_call("-transparentcolor", "white")
            # Should set always on top
            mock_root.attributes.assert_any_call("-topmost", True)
            # Should remove borders
            mock_root.overrideredirect.assert_called_once_with(True)
