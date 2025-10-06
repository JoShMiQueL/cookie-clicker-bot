"""Setup script for Cookie Clicker Bot."""

import subprocess
import sys

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        install_hooks()


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        install_hooks()


def install_hooks():
    """Install pre-commit hooks automatically."""
    try:
        print("\n🔧 Installing pre-commit hooks...")
        subprocess.check_call([sys.executable, "-m", "pre_commit", "install"])
        subprocess.check_call([sys.executable, "-m", "pre_commit", "install", "--hook-type", "commit-msg"])
        print("✅ Pre-commit hooks installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Could not install pre-commit hooks: {e}")
        print("   You can install them manually with: pre-commit install")


setup(
    name="cookie-clicker-bot",
    version="1.0.0",
    author="JoShMiQueL",
    author_email="joshmiqueldev@gmail.com",
    description="Professional autoclicker for Cookie Clicker with GUI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JoShMiQueL/cookie-clicker-bot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.8",
    install_requires=[
        "keyboard>=0.13.5",
        "pywin32>=306; sys_platform == 'win32'",
    ],
    extras_require={
        "dev": [
            "ruff>=0.1.0",
            "pyinstaller>=6.0.0",
            "pre-commit>=3.5.0",
        ],
    },
    cmdclass={
        "develop": PostDevelopCommand,
        "install": PostInstallCommand,
    },
)
