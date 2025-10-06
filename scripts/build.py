"""Build script for creating the executable."""

import subprocess
import sys
from pathlib import Path


def build_executable():
    """Build the executable using PyInstaller."""
    print("🔨 Building Cookie Clicker Autoclicker...")
    print("=" * 60)

    spec_file = Path(__file__).parent / "CookieClickerBot.spec"

    if not spec_file.exists():
        print(f"❌ Spec file not found: {spec_file}")
        sys.exit(1)

    try:
        subprocess.check_call([sys.executable, "-m", "PyInstaller", str(spec_file), "--clean"])
        print("\n" + "=" * 60)
        print("✅ Build successful!")
        print("📁 Executable: dist/CookieClickerBot.exe")
        print("=" * 60)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_executable()
