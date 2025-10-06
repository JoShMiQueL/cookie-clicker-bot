# Test Suite

This directory contains the comprehensive test suite for the Cookie Clicker Bot.

## Structure

```
tests/
├── __init__.py           # Test package initialization
├── conftest.py           # Pytest fixtures and configuration
├── test_config.py        # Configuration module tests
├── test_window_finder.py # Window finder tests
├── test_clicker.py       # Autoclicker tests
├── test_overlay.py       # Overlay tests
└── test_gui.py           # GUI tests
```

## Running Tests

### Install Test Dependencies

```bash
pip install -e ".[test]"
```

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_config.py
```

### Run Specific Test

```bash
pytest tests/test_config.py::TestConfig::test_cps_default_value
```

### Run with Coverage

```bash
pytest --cov=src --cov-report=html
```

This will generate an HTML coverage report in `htmlcov/index.html`.

### Run with Verbose Output

```bash
pytest -v
```

### Run Only Fast Tests (exclude slow tests)

```bash
pytest -m "not slow"
```

## Test Coverage

The test suite covers:

- **Configuration (`test_config.py`)**: Tests for all configuration values and their constraints
- **Window Finder (`test_window_finder.py`)**: Tests for Cookie Clicker window detection with various title formats
- **Autoclicker (`test_clicker.py`)**: Tests for click sending, position calculation, and CPS management
- **Overlay (`test_overlay.py`)**: Tests for visual overlay creation and positioning
- **GUI (`test_gui.py`)**: Tests for GUI initialization, controls, and real-time updates

## Mocking Strategy

The tests use extensive mocking to avoid dependencies on:
- Windows-specific APIs (`win32gui`, `win32api`, `win32con`)
- Tkinter GUI components
- Threading and timing operations

This allows tests to run quickly and reliably without requiring a Windows environment or actual GUI interaction.

## Writing New Tests

When adding new tests:

1. Follow the existing naming convention: `test_*.py`
2. Use descriptive test names that explain what is being tested
3. Use fixtures from `conftest.py` for common setup
4. Mock external dependencies appropriately
5. Add docstrings to test classes and methods
6. Group related tests in classes

Example:

```python
class TestNewFeature:
    """Test new feature functionality."""

    @pytest.fixture
    def feature(self):
        """Create a feature instance."""
        return NewFeature()

    def test_feature_initialization(self, feature):
        """Test that feature initializes correctly."""
        assert feature.is_ready is True
```

## Continuous Integration

These tests are automatically run in CI/CD pipelines on:
- Pull requests
- Pushes to main branch
- Release workflows

See `.github/workflows/pr-checks.yml` for CI configuration.
