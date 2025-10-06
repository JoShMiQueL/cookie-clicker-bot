"""Build script for creating the executable."""

import os
import subprocess
import sys
from pathlib import Path


def build_executable():
    """Build the executable using PyInstaller."""
    print("🔨 Building Cookie Clicker Autoclicker...")
    print("=" * 60)

    # Spec file is in the project root, not in scripts/
    # __file__ is scripts/build.py, so parent.parent gets us to project root
    project_root = Path(__file__).resolve().parent.parent
    spec_file = project_root / "CookieClickerBot.spec"

    if not spec_file.exists():
        print(f"❌ Spec file not found: {spec_file}")
        sys.exit(1)

    # Change to project root directory (required for PyInstaller)
    original_dir = Path.cwd()
    os.chdir(project_root)

    try:
        subprocess.check_call([sys.executable, "-m", "PyInstaller", spec_file.name, "--clean"])
        print("\n" + "=" * 60)
        print("✅ Build successful!")
        print("📁 Executable: dist/CookieClickerBot.exe")
        print("=" * 60)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        sys.exit(1)
    finally:
        # Return to original directory
        os.chdir(original_dir)


if __name__ == "__main__":
    build_executable()
