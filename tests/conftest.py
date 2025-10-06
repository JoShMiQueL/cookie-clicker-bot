"""Pytest configuration and fixtures."""

import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest


# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def mock_win32gui(monkeypatch):
    """Mock win32gui module."""
    mock = MagicMock()
    mock.GetClientRect.return_value = (0, 0, 1000, 800)
    mock.ClientToScreen.return_value = (500, 400)
    mock.IsWindowVisible.return_value = True
    mock.GetWindowText.return_value = "245 cookies - Cookie Clicker"
    monkeypatch.setattr("win32gui.GetClientRect", mock.GetClientRect)
    monkeypatch.setattr("win32gui.ClientToScreen", mock.ClientToScreen)
    monkeypatch.setattr("win32gui.IsWindowVisible", mock.IsWindowVisible)
    monkeypatch.setattr("win32gui.GetWindowText", mock.GetWindowText)
    monkeypatch.setattr("win32gui.EnumWindows", lambda callback, arg: callback(12345, arg))
    return mock


@pytest.fixture
def mock_win32api(monkeypatch):
    """Mock win32api module."""
    mock = MagicMock()
    monkeypatch.setattr("win32api.SendMessage", mock.SendMessage)
    return mock


@pytest.fixture
def mock_win32con(monkeypatch):
    """Mock win32con module."""
    mock = MagicMock()
    mock.WM_LBUTTONDOWN = 0x0201
    mock.WM_LBUTTONUP = 0x0202
    mock.MK_LBUTTON = 0x0001
    monkeypatch.setattr("win32con.WM_LBUTTONDOWN", mock.WM_LBUTTONDOWN)
    monkeypatch.setattr("win32con.WM_LBUTTONUP", mock.WM_LBUTTONUP)
    monkeypatch.setattr("win32con.MK_LBUTTON", mock.MK_LBUTTON)
    return mock


@pytest.fixture
def mock_threading_event():
    """Create a mock threading event."""
    import threading

    return threading.Event()
