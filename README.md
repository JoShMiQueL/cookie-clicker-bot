# 🍪 Cookie Clicker Autoclicker

[![Build Status](https://github.com/JoShMiQueL/cookie-clicker-bot/workflows/CI%20Pipeline/badge.svg)](https://github.com/JoShMiQueL/cookie-clicker-bot/actions/workflows/ci-pipeline.yml)
[![Tests](https://github.com/JoShMiQueL/cookie-clicker-bot/workflows/Tests/badge.svg)](https://github.com/JoShMiQueL/cookie-clicker-bot/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

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

## 🚀 Quick Start

### For End Users (Easiest)

1. **Download** `CookieClickerBot.exe` from [Releases](https://github.com/JoShMiQueL/cookie-clicker-bot/releases)
2. **Run** the executable (no installation needed!)
3. **Use:**
   - Open Cookie Clicker in Steam (windowed mode)
   - Click "Start" in the bot
   - Adjust settings in real-time
   - Click "Stop" when done

### For Developers

```bash
# Clone and setup
git clone https://github.com/JoShMiQueL/cookie-clicker-bot.git
cd cookie-clicker-bot

# Install in development mode
pip install -e ".[dev]"

# Setup pre-commit hooks
setup-hooks

# Run GUI
python main.py

# Run tests
pytest
# Or with coverage
pytest --cov=src --cov-report=html
```

**Build executable:**
```bash
python scripts/build.py
# Find in dist/CookieClickerBot.exe
```

## 🧪 Testing

This project includes a comprehensive test suite with high coverage (47 tests).

**Quick test run:**
```bash
# Windows
.\scripts\run_tests.ps1

# Linux/Mac
./scripts/run_tests.sh

# Or directly with pytest
pytest
```

**Run with coverage report:**
```bash
pytest --cov=src --cov-report=html
# Open htmlcov/index.html to view detailed coverage
```

**Run specific test file:**
```bash
pytest tests/test_clicker.py
```

**Test structure:**
- `tests/test_config.py` - Configuration tests (8 tests)
- `tests/test_window_finder.py` - Window detection tests (14 tests)
- `tests/test_clicker.py` - Autoclicker logic tests (12 tests)
- `tests/test_overlay.py` - Visual overlay tests (9 tests)
- `tests/test_gui.py` - GUI functionality tests (4 tests)

**Automated testing:**
Tests are automatically run:
- ✅ **Before every push** (via pre-push hook)
- ✅ **On every pull request** (with coverage reporting)
- ✅ **On every push to main** (on Ubuntu and Windows)

See [tests/README.md](tests/README.md) for detailed testing documentation.

## 💡 Usage Tips

### Finding the Right Position

1. Start the bot with overlay enabled
2. See the red dot indicator
3. Adjust X/Y sliders in real-time
4. Watch the overlay move
5. Fine-tune until it's on the cookie

### Optimal Settings

- **CPS**: 15-20 for best performance
- **Position**: Adjust based on window size
- **Overlay**: Enable for initial setup, disable for performance

### Troubleshooting

**Bot doesn't find the game?**
- Make sure Cookie Clicker is running
- Use windowed mode (not fullscreen)
- Check the window title matches one of these patterns:
  - `245 cookies - Cookie Clicker`
  - `72.197 million cookies - Cookie Clicker`
  - `13.564 billion cookies - Cookie Clicker`

**Clicks in wrong position?**
- Enable overlay to see where it clicks
- Adjust X/Y position sliders
- Changes apply in real-time

**Bot stops immediately?**
- Run as administrator for better compatibility
- Check antivirus isn't blocking it

## 🏗️ Project Structure

```
cookie-clicker-bot/
├── main.py                   # GUI application entry point
├── src/                      # Source code
│   ├── __init__.py
│   ├── config.py             # Configuration
│   ├── window_finder.py      # Window detection
│   ├── clicker.py            # Click automation
│   ├── overlay.py            # Visual overlay
│   └── gui.py                # GUI implementation
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures
│   ├── test_config.py        # Config tests
│   ├── test_window_finder.py # Window finder tests
│   ├── test_clicker.py       # Clicker tests
│   ├── test_overlay.py       # Overlay tests
│   ├── test_gui.py           # GUI tests
│   └── README.md             # Testing documentation
├── scripts/                  # Utility scripts
│   ├── build.py              # Build executable
│   └── setup_hooks.py        # Pre-commit hooks setup
├── .github/                  # GitHub configuration
│   ├── workflows/            # CI/CD pipelines
│   │   ├── ci-pipeline.yml   # Main CI/CD pipeline
│   │   ├── pr-checks.yml     # PR validation (includes tests)
│   │   ├── tests.yml         # Test suite execution
│   │   ├── pr-labeler.yml    # PR labeling & stats
│   │   ├── release.yml       # Automated releases
│   │   ├── changelog.yml     # Changelog generation
│   │   ├── codeql.yml        # Security analysis
│   │   ├── stale.yml         # Stale issues/PRs
│   │   ├── auto-merge.yml    # Dependabot auto-merge
│   │   └── welcome.yml       # Welcome contributors
│   ├── ISSUE_TEMPLATE/       # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── WORKFLOWS.md          # Workflows documentation
│   ├── CONVENTIONAL_COMMITS.md
│   ├── labeler.yml           # PR label configuration
│   └── labels.yml            # Label definitions
├── .pre-commit-config.yaml   # Pre-commit hooks config
├── .commitlintrc.json        # Commitlint configuration
├── .gitignore                # Git ignore rules
├── CookieClickerBot.spec     # PyInstaller configuration
├── pyproject.toml            # Project configuration
├── ruff.toml                 # Ruff linter configuration
├── CONTRIBUTING.md           # Contribution guidelines
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## 🛠️ Development

### Quick Setup

```bash
pip install -e ".[dev]"  # Install with dev dependencies
setup-hooks               # Setup pre-commit hooks
```

**For detailed development instructions, see [CONTRIBUTING.md](CONTRIBUTING.md)**

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

## ⚙️ Configuration

Edit `src/config.py`:

```python
CPS = 15                      # Clicks per second (1-50)
BIG_COOKIE_RELATIVE_X = 0.15  # X position (0.0-1.0)
BIG_COOKIE_RELATIVE_Y = 0.39  # Y position (0.0-1.0)
SHOW_OVERLAY = True           # Show visual indicator
STOP_KEY = "f1"               # Stop key (CLI only)
```

## 🤖 CI/CD Pipeline

### Automated Workflows

#### **Code Quality**
- **CI** (`ci.yml`) - Runs pre-commit checks on every push/PR
- **CodeQL** (`codeql.yml`) - Security analysis (weekly + on push)
- **Dependency Review** (`dependency-review.yml`) - Reviews dependency changes in PRs

#### **Build & Release**
- **Build** (`build.yml`) - Builds executable on push to main/develop
  - Comments PR with build size and checksum
  - Uploads artifacts for testing

- **Release** (`release.yml`) - Automated releases
  - **Tags** (`v*.*.*`) → Production release
  - **Tags** (`v*.*.*-beta.*`) → Beta release
  - **Tags** (`v*.*.*-alpha.*`) → Alpha release
  - **Tags** (`v*.*.*-rc.*`) → Release candidate
  - **Manual trigger** → Custom version release
  - Includes SHA256 checksums
  - Auto-updates `latest` tag for production releases

- **Changelog** (`changelog.yml`) - Auto-generates changelog on tags

#### **PR Automation**
- **PR Labeler** (`pr-labeler.yml`)
  - Auto-labels by size (XS, S, M, L, XL)
  - Labels by area (gui, core, build, ci, docs)
  - Labels by conventional commit type
  - Detects breaking changes

- **PR Checks** (`pr-checks.yml`)
  - Validates PR title (conventional commits)
  - Checks for merge conflicts
  - Validates branch naming convention
  - Checks for linked issues

#### **Maintenance**
- **Stale** (`stale.yml`) - Marks inactive issues/PRs as stale
- **Auto-merge** (`auto-merge.yml`) - Auto-merges Dependabot PRs (patch/minor)
- **Welcome** (`welcome.yml`) - Welcomes first-time contributors

### Creating a Release

**Production Release:**
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

**Beta Release:**
```bash
git tag -a v1.0.0-beta.1 -m "Beta release 1.0.0-beta.1"
git push origin v1.0.0-beta.1
```

**Alpha Release:**
```bash
git tag -a v1.0.0-alpha.1 -m "Alpha release 1.0.0-alpha.1"
git push origin v1.0.0-alpha.1
```

**Release Candidate:**
```bash
git tag -a v1.0.0-rc.1 -m "Release candidate 1.0.0-rc.1"
git push origin v1.0.0-rc.1
```

**Manual Release (via GitHub UI):**
1. Go to Actions → Release
2. Click "Run workflow"
3. Enter version (e.g., `v1.0.0-beta.1`)
4. Check "Mark as pre-release" if needed
5. Click "Run workflow"

### Branch Naming Convention

**Required format:** `type/description`

**Valid types:**
- `feat/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation
- `style/` - Code style
- `refactor/` - Refactoring
- `perf/` - Performance
- `test/` - Tests
- `build/` - Build system
- `ci/` - CI/CD
- `chore/` - Maintenance
- `hotfix/` - Hotfixes

**Rules:**
- Use lowercase letters, numbers, and hyphens only
- Minimum 5 characters
- Examples: `feat/add-overlay`, `fix/button-click`

## 📝 Contributing

We welcome contributions! This project follows strict standards to maintain code quality.

### Quick Start

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Commit using **Conventional Commits** (required)
5. Push and open a Pull Request

### Requirements

⚠️ **Conventional Commits are REQUIRED** - All commits and PR titles must follow the [Conventional Commits](https://conventionalcommits.org/) specification.

**Quick Reference:**
```bash
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug"
git commit -m "docs: update readme"
```

**See:**
- 📖 [CONTRIBUTING.md](CONTRIBUTING.md) - Full contribution guide
- 📝 [Conventional Commits Guide](.github/CONVENTIONAL_COMMITS.md) - Detailed commit format reference
- 🔧 [Workflows Documentation](.github/WORKFLOWS.md) - CI/CD and automation

**Note:** PRs with invalid commit formats will be automatically rejected by CI.

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
