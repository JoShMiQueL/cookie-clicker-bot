# 🍪 Cookie Clicker Autoclicker

[![Build Status](https://github.com/JoShMiQueL/cookie-clicker-bot/workflows/Build%20Executable/badge.svg)](https://github.com/JoShMiQueL/cookie-clicker-bot/actions)
[![Lint Status](https://github.com/JoShMiQueL/cookie-clicker-bot/workflows/Lint%20and%20Format/badge.svg)](https://github.com/JoShMiQueL/cookie-clicker-bot/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

Professional autoclicker for Cookie Clicker (Steam) with graphical interface, real-time adjustments, and visual overlay.

> ⚠️ **Educational Purpose**: This tool is for educational purposes only. Use at your own risk.

## ✨ Features

- **🎨 Intuitive GUI**: Easy-to-use graphical interface
- **⚡ Real-time Adjustments**: Modify CPS and position while the bot is running
- **🎯 Visual Overlay**: Transparent indicator showing exactly where clicks are made
- **🔄 Live Updates**: Overlay moves in real-time when adjusting position
- **🖱️ Non-intrusive**: Doesn't affect your physical cursor
- **🪟 Background Operation**: Works while you use other windows
- **🔍 Auto-detection**: Automatically finds the Cookie Clicker window
- **🏗️ Professional Architecture**: Modular design following SOLID principles

## 📦 Installation

### Option 1: Download Executable (Easiest)

1. Go to [Releases](https://github.com/JoShMiQueL/cookie-clicker-bot/releases)
2. Download `CookieClickerBot.exe` from the latest release
3. Run the executable (no Python installation required)

### Option 2: From Source

```bash
# Clone the repository
git clone https://github.com/JoShMiQueL/cookie-clicker-bot.git
cd cookie-clicker-bot

# Install dependencies
pip install -r requirements.txt

# Run the GUI (option 1 - module)
python -m src.gui

# Run the GUI (option 2 - script)
python scripts/run_gui.py

# Or run the CLI version
python -m src.main
python scripts/run_cli.py
```

## 🚀 Usage

### GUI Version (Recommended)

1. Open Cookie Clicker in Steam (windowed mode recommended)
2. Run `CookieClickerBot.exe` or `python -m src.gui`
3. Adjust settings in the interface:
   - **CPS**: Clicks per second (1-50)
   - **Position X/Y**: Adjust click position (0.0-1.0)
   - **Visual Overlay**: Enable/disable visual indicator
4. Click **▶ Start** to begin
5. **Real-time adjustments**: Modify settings while the bot is active
6. Click **⏹ Stop** when done

### CLI Version

```bash
# Edit src/config.py to adjust settings
python -m src.main

# Press F1 to stop
```

## 🏗️ Project Structure

```
cookie-clicker-bot/
├── src/                      # Source code
│   ├── __init__.py
│   ├── config.py
│   ├── window_finder.py
│   ├── clicker.py
│   ├── overlay.py
│   ├── gui.py
│   └── main.py
├── scripts/                  # Utility scripts
│   ├── build.py              # Build executable
│   └── setup_dev.py          # Setup dev environment
├── .github/                  # GitHub configuration
│   ├── workflows/            # CI/CD pipelines
│   │   ├── lint.yml          # Linting and formatting
│   │   ├── build.yml         # Build automation
│   │   ├── release.yml       # Release automation
│   │   ├── changelog.yml     # Changelog generation
│   │   └── pr-labeler.yml    # PR auto-labeling
│   └── labeler.yml           # PR label configuration
├── .pre-commit-config.yaml   # Pre-commit hooks config
├── CookieClickerBot.spec     # PyInstaller configuration
├── cliff.toml                # Changelog generator config
├── pyproject.toml            # Project configuration
├── requirements.txt          # Runtime dependencies
├── requirements-dev.txt      # Development dependencies
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── README.md                 # This file
```

## 🛠️ Development

### Setup Development Environment

```bash
# Install in development mode (hooks install automatically)
pip install -e ".[dev]"
```

This will:
- Install all dependencies
- Install development tools (ruff, pre-commit, pyinstaller)
- **Automatically setup pre-commit hooks**
- You're ready to develop!

Alternative manual setup:
```bash
pip install -r requirements-dev.txt
pre-commit install
pre-commit install --hook-type commit-msg
```

### Git Hooks (Automatic)

The project uses **pre-commit** framework (like Husky for Python):

**What happens automatically:**
- ✨ **Auto-format code** with Ruff before commit
- 🔍 **Lint code** and auto-fix issues
- 📝 **Validate commit messages** (conventional commits)
- ✅ **Run all checks** before push

**Manual commands:**
```bash
# Run all hooks manually
pre-commit run --all-files

# Run specific hook
pre-commit run ruff-format --all-files

# Skip hooks (not recommended)
git commit --no-verify
```

### Code Quality

This project uses:
- **Ruff** for linting and formatting
- **GitHub Actions** for CI/CD
- **Automated PR labeling** based on changed files
- **Automated releases** with changelog generation

## 🔧 Configuration

Edit `src/config.py` to customize:

```python
CPS = 15                      # Clicks per second
BIG_COOKIE_RELATIVE_X = 0.15  # X position (0.0-1.0)
BIG_COOKIE_RELATIVE_Y = 0.39  # Y position (0.0-1.0)
SHOW_OVERLAY = True           # Show visual overlay
STOP_KEY = "f1"               # Stop key (CLI only)
```

## 🤖 CI/CD Pipeline

### Automated Workflows

1. **Lint & Format** (`lint.yml`)
   - Runs on every push and PR
   - Checks code style with Ruff
   - Ensures consistent formatting

2. **Build** (`build.yml`)
   - Builds executable on every push to main
   - Uploads artifacts for testing
   - Generates checksums for releases

3. **Release** (`release.yml`)
   - Triggers on version tags (v*)
   - Builds and publishes executable
   - Generates changelog automatically
   - Creates GitHub release with notes

4. **PR Labeler** (`pr-labeler.yml`)
   - Auto-labels PRs based on changed files
   - Adds size labels (XS, S, M, L, XL)
   - Categorizes by area (gui, core, cli)

### Creating a Release

```bash
# Tag a new version
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# GitHub Actions will automatically:
# 1. Build the executable
# 2. Generate changelog
# 3. Create release with notes
# 4. Upload executable and checksum
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Build/tooling changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Use at your own risk. The authors are not responsible for any consequences of using this software.

## 🙏 Acknowledgments

- Cookie Clicker by [Orteil](https://orteil.dashnet.org/cookieclicker/)
- Built with Python and tkinter
- Automated with GitHub Actions

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/JoShMiQueL/cookie-clicker-bot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JoShMiQueL/cookie-clicker-bot/discussions)
- **Security**: See [SECURITY.md](.github/SECURITY.md)

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 Code of Conduct

Please read [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md) before contributing.

---

Made with ❤️ by [JoShMiQueL](https://github.com/JoShMiQueL)
