# Contributing to Cookie Clicker Autoclicker

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/JoShMiQueL/cookie-clicker-bot.git`
3. Setup development environment: `pip install -e ".[dev]"` (hooks install automatically)
4. Create a branch: `git checkout -b feature/your-feature-name`
5. Make your changes (code will auto-format on commit)
6. Commit using conventional commits (enforced automatically)
7. Push and create a Pull Request

## 📝 Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/) for clear and structured commit history.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system or external dependencies
- `ci`: CI/CD configuration changes
- `chore`: Other changes that don't modify src or test files

### Examples

```bash
feat(gui): add dark mode support
fix(clicker): correct click position calculation
docs: update installation instructions
refactor(overlay): simplify position update logic
```

## 🧪 Code Quality

### Linting and Formatting

We use **Ruff** for both linting and formatting:

```bash
# Check linting
ruff check src/

# Fix linting issues automatically
ruff check --fix src/

# Check formatting
ruff format --check src/

# Apply formatting
ruff format src/
```

### Before Submitting

The pre-commit hooks will automatically:
- Format your code with Ruff
- Run linting checks
- Validate commit message format
- Run all checks before push

**Manual checks (optional):**
```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Test the build
python scripts/build.py

# Test the application
python -m src.gui
python -m src.main
```

**Note:** If you need to skip hooks (not recommended):
```bash
git commit --no-verify
```

## 🏗️ Project Structure

```
src/
├── __init__.py          # Package initialization
├── config.py            # Configuration
├── window_finder.py     # Window detection
├── clicker.py           # Click automation
├── overlay.py           # Visual overlay
├── gui.py               # GUI application
└── main.py              # CLI application
```

## 📋 Pull Request Process

1. **Update documentation** if you're adding features
2. **Add tests** if applicable
3. **Follow the code style** (enforced by Ruff)
4. **Write clear commit messages** using conventional commits
5. **Update CHANGELOG.md** if making significant changes
6. **Ensure CI passes** before requesting review

### PR Title Format

Use the same format as commits:

```
feat(gui): add dark mode support
fix(clicker): correct click position calculation
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
```

## 🐛 Reporting Bugs

Use the [GitHub Issues](https://github.com/yourusername/cookie-clicker-bot/issues) page.

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g., Windows 11]
 - Python Version: [e.g., 3.11]
 - Version: [e.g., 1.0.0]

**Additional context**
Any other context about the problem.
```

## 💡 Feature Requests

We welcome feature requests! Please use GitHub Issues with the "enhancement" label.

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Any other context or screenshots.
```

## 🎨 Code Style

- **Line length**: 120 characters
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Imports**: Sorted alphabetically, grouped by standard/external/local
- **Docstrings**: Google style
- **Type hints**: Use type hints for function parameters and returns

### Example

```python
"""Module description."""

import threading
from typing import Optional

import win32gui

from . import config


class MyClass:
    """Class description.

    Attributes:
        attribute: Description of attribute.
    """

    def __init__(self, param: int):
        """Initialize the class.

        Args:
            param: Description of parameter.
        """
        self.attribute = param

    def my_method(self, value: str) -> Optional[int]:
        """Method description.

        Args:
            value: Description of value.

        Returns:
            Description of return value.
        """
        return len(value) if value else None
```

## 📚 Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add comments for complex logic
- Update CHANGELOG.md for notable changes

## 🔄 Release Process

Releases are automated via GitHub Actions:

1. Update version in `src/__init__.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Commit changes: `git commit -m "chore: bump version to 1.1.0"`
4. Create tag: `git tag -a v1.1.0 -m "Release version 1.1.0"`
5. Push: `git push origin main --tags`
6. GitHub Actions will automatically build and create the release

## ❓ Questions?

Feel free to open a [Discussion](https://github.com/yourusername/cookie-clicker-bot/discussions) if you have questions!

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.
