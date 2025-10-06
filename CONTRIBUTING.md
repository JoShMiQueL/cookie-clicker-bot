# Contributing to Cookie Clicker Bot

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Branch Naming](#branch-naming)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/cookie-clicker-bot.git
   cd cookie-clicker-bot
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/JoShMiQueL/cookie-clicker-bot.git
   ```

## Development Setup

### Prerequisites

- Python 3.12+
- Git
- Windows OS (for testing the autoclicker)

### Installation

```bash
# 1. Install in development mode
pip install -e ".[dev]"

# 2. Setup pre-commit hooks
setup-hooks
```

This will:
- Install all dependencies
- Install development tools (ruff, pre-commit, pyinstaller)
- Configure pre-commit and commit-msg hooks
- You're ready to develop!

### Verify Setup

```bash
# Run linting
ruff check .

# Run formatting
ruff format .

# Run pre-commit on all files
pre-commit run --all-files
```

## Coding Standards

### Python Style

- **Python Version**: 3.12+
- **Formatter**: Ruff
- **Linter**: Ruff
- **Line Length**: 100 characters
- **Docstrings**: Required for all public functions/classes
- **Type Hints**: Encouraged but not required

### Code Quality

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Keep functions small and focused
- Add comments for complex logic
- Remove unused imports and variables

### Pre-commit Hooks

Pre-commit hooks will automatically:
- Format code with Ruff
- Lint code and auto-fix issues
- Validate YAML/TOML files
- Check for trailing whitespace
- Validate commit messages

**To skip hooks** (not recommended):
```bash
git commit --no-verify
```

## Commit Guidelines

### **REQUIRED: Conventional Commits**

This project **strictly enforces** [Conventional Commits](https://conventionalcommits.org/).

**Format:** `type(scope): description`

**Quick Examples:**
```bash
git commit -m "feat: add click counter"
git commit -m "fix(gui): resolve button alignment"
git commit -m "docs: update installation guide"
git commit -m "feat!: change config format"  # Breaking change
```

**📖 For complete guide with all types, scopes, examples, and troubleshooting:**
- See [.github/CONVENTIONAL_COMMITS.md](.github/CONVENTIONAL_COMMITS.md)

**Validation:**
- ✅ Pre-commit hook validates locally
- ✅ CI validates PR title and all commits
- ❌ Invalid commits will be rejected

## Branch Naming

### **REQUIRED Format**

```
<type>/<description>
```

### Rules

- **Type**: Must be one of the conventional commit types
- **Description**:
  - Lowercase letters, numbers, and hyphens only
  - Minimum 5 characters
  - Descriptive and concise

### Examples

✅ **Valid:**
```bash
feat/add-overlay
fix/button-click
docs/update-readme
refactor/simplify-logic
```

❌ **Invalid:**
```bash
feature/AddOverlay      # Wrong type, wrong case
fix-button              # Missing slash
feat/abc                # Too short
my-branch               # Missing type
```

### Creating a Branch

```bash
# From main/develop
git checkout -b feat/your-feature-name
```

## Pull Request Process

### Before Creating a PR

1. **Update your fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run all checks**:
   ```bash
   pre-commit run --all-files
   ruff check .
   ruff format .
   ```

3. **Test your changes** locally

### Creating a PR

1. **Push your branch**:
   ```bash
   git push origin feat/your-feature-name
   ```

2. **Open a Pull Request** on GitHub

3. **Fill out the PR template** completely

4. **Ensure PR title follows conventional commits**:
   ```
   feat: add new feature
   fix: resolve bug
   docs: update documentation
   ```

### PR Requirements

Your PR must:

- ✅ Have a **conventional commit title**
- ✅ Have a **clear description**
- ✅ **Link to an issue** (if applicable)
- ✅ Pass **all CI checks**
- ✅ Have **no merge conflicts**
- ✅ Follow **branch naming convention**
- ✅ Include **tests** (if applicable)
- ✅ Update **documentation** (if needed)

### PR Review Process

1. **Automated checks** run on your PR
2. **Maintainer review** - May request changes
3. **Address feedback** - Push updates to your branch
4. **Approval** - Once approved, PR will be merged
5. **Squash and merge** - Commits are squashed with conventional commit message

### After Merge

1. **Delete your branch**:
   ```bash
   git branch -d feat/your-feature-name
   git push origin --delete feat/your-feature-name
   ```

2. **Update your fork**:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

## Testing

### Running Tests

```bash
# Run all tests (when available)
pytest

# Run specific test
pytest tests/test_clicker.py

# Run with coverage
pytest --cov
```

### Writing Tests

- Add tests for new features
- Update tests for bug fixes
- Ensure tests are descriptive
- Use meaningful test names

## Questions?

- **Issues**: [GitHub Issues](https://github.com/JoShMiQueL/cookie-clicker-bot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/JoShMiQueL/cookie-clicker-bot/discussions)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🎉**
