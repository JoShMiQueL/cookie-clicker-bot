"""Pre-commit hooks installation utility."""

import subprocess
import sys
from pathlib import Path


def install_hooks():
    """Install pre-commit hooks if in a git repository."""
    if not Path(".git").exists():
        print("⚠ Not a git repository, skipping pre-commit hooks installation")
        return

    try:
        subprocess.run(
            ["pre-commit", "install", "--install-hooks"],
            check=True,
        )
        print("✓ Pre-commit hooks installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install pre-commit hooks: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(
            '✗ pre-commit not found. Install dev dependencies first:\n  pip install -e ".[dev]"',
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    """Entry point for setup-hooks command."""
    install_hooks()


if __name__ == "__main__":
    main()
