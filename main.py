"""Entry point for the GUI application."""

import sys
from pathlib import Path


# Add src to path so imports work
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import after path setup (required for PyInstaller)
from src.gui import AutoClickerGUI  # noqa: E402


if __name__ == "__main__":
    app = AutoClickerGUI()
    app.run()
