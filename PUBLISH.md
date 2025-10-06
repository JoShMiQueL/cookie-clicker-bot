# Publishing Guide

This guide explains how to publish the Cookie Clicker Bot to GitHub.

## 📋 Pre-Publication Checklist

- [ ] All code is in English
- [ ] All tests pass
- [ ] Documentation is complete
- [ ] LICENSE file is present
- [ ] .gitignore is configured
- [ ] Pre-commit hooks are configured
- [ ] GitHub Actions workflows are ready

## 🚀 Initial Publication

### Step 1: Initialize Git Repository

```bash
# Initialize Git (if not already done)
git init
git branch -M main
```

### Step 2: Setup Development Environment

```bash
# Install in development mode (hooks install automatically)
pip install -e ".[dev]"
```

This will:
- Install all dependencies
- Install development tools
- **Automatically setup pre-commit hooks**
- Run initial formatting on all files

### Step 3: Create Initial Commit

```bash
# Add all files
git add .

# Create initial commit (pre-commit hooks will run automatically)
git commit -m "feat: initial commit with professional structure"
```

### Step 4: Create GitHub Repository

Go to https://github.com/new and create a new repository:
- **Repository name**: `cookie-clicker-bot`
- **Description**: `Professional autoclicker for Cookie Clicker with GUI and real-time adjustments`
- **Visibility**: Public
- **DO NOT** initialize with README, .gitignore, or license (we already have them)

### Step 5: Push to GitHub

```bash
# Add remote
git remote add origin https://github.com/JoShMiQueL/cookie-clicker-bot.git

# Push to GitHub
git push -u origin main
```

### Alternative: Using GitHub CLI

```bash
# Create and push in one command
gh repo create cookie-clicker-bot --public --source=. --remote=origin --push
```

## 🏷️ Creating Your First Release

### 1. Update Version

Update version in:
- `src/__init__.py`
- `pyproject.toml`

### 2. Create and Push Tag

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0
```

### 3. Automatic Release

GitHub Actions will automatically:
- Build the executable
- Generate changelog
- Create GitHub release
- Upload executable and checksum

## 📝 Post-Publication Tasks

### 1. Enable GitHub Features

Go to repository settings and enable:
- [ ] Issues
- [ ] Discussions (optional)
- [ ] Wikis (optional)
- [ ] Projects (optional)

### 2. Configure Branch Protection

Settings → Branches → Add rule for `main`:
- [ ] Require pull request reviews
- [ ] Require status checks to pass
- [ ] Require conversation resolution
- [ ] Include administrators

### 3. Add Topics

Add repository topics:
- `cookie-clicker`
- `autoclicker`
- `bot`
- `python`
- `automation`
- `gaming`
- `tkinter`

### 4. Add Description and Website

- **Description**: Professional autoclicker for Cookie Clicker with GUI and real-time adjustments
- **Website**: (optional) Link to documentation or demo

### 5. Create About Section

Fill in:
- Description
- Topics
- License: MIT
- Releases: Link to latest release

## 🔄 Ongoing Maintenance

### Creating New Releases

```bash
# 1. Make your changes
git add .
git commit -m "feat: add new feature"

# 2. Update version numbers
# Edit src/__init__.py and pyproject.toml

# 3. Create tag
git tag -a v1.1.0 -m "Release version 1.1.0"

# 4. Push
git push origin main --tags
```

### Managing Issues

- Use issue templates (already configured)
- Label issues appropriately
- Link PRs to issues
- Close issues when resolved

### Managing Pull Requests

- Use PR template (already configured)
- Require reviews
- Run CI checks
- Squash and merge

## 📊 Monitoring

### GitHub Actions

Monitor workflows at:
`https://github.com/JoShMiQueL/cookie-clicker-bot/actions`

### Insights

Check repository insights:
- Traffic
- Contributors
- Community
- Dependency graph

## 🎯 Best Practices

1. **Semantic Versioning**: Use MAJOR.MINOR.PATCH
2. **Conventional Commits**: Enforced by pre-commit hooks
3. **Changelog**: Auto-generated on releases
4. **Security**: Report vulnerabilities via SECURITY.md
5. **Code of Conduct**: Follow CODE_OF_CONDUCT.md

## 🆘 Troubleshooting

### GitHub Actions Failing

1. Check workflow logs
2. Verify secrets are set (if any)
3. Test locally first
4. Check Python version compatibility

### Pre-commit Hooks Not Working

```bash
# Reinstall hooks
pre-commit uninstall
pre-commit install
pre-commit install --hook-type commit-msg
```

### Build Failing

```bash
# Test build locally
python scripts/build.py

# Check PyInstaller version
pip install --upgrade pyinstaller
```

## 📚 Resources

- [GitHub Docs](https://docs.github.com)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)

---

Ready to publish? Follow the steps above to get started! 🚀
