"""Tests for configuration module."""

from src import config


class TestConfig:
    """Test configuration values and constraints."""

    def test_cps_default_value(self):
        """Test that CPS has a valid default value."""
        assert config.CPS > 0
        assert isinstance(config.CPS, int)

    def test_cps_reasonable_range(self):
        """Test that CPS is within a reasonable range."""
        assert 1 <= config.CPS <= 100

    def test_big_cookie_relative_x_range(self):
        """Test that X position is within valid range."""
        assert 0.0 <= config.BIG_COOKIE_RELATIVE_X <= 1.0

    def test_big_cookie_relative_y_range(self):
        """Test that Y position is within valid range."""
        assert 0.0 <= config.BIG_COOKIE_RELATIVE_Y <= 1.0

    def test_show_overlay_is_boolean(self):
        """Test that SHOW_OVERLAY is a boolean."""
        assert isinstance(config.SHOW_OVERLAY, bool)

    def test_stop_key_is_string(self):
        """Test that STOP_KEY is a string."""
        assert isinstance(config.STOP_KEY, str)
        assert len(config.STOP_KEY) > 0

    def test_config_values_are_accessible(self):
        """Test that all config values can be accessed."""
        assert hasattr(config, "CPS")
        assert hasattr(config, "BIG_COOKIE_RELATIVE_X")
        assert hasattr(config, "BIG_COOKIE_RELATIVE_Y")
        assert hasattr(config, "SHOW_OVERLAY")
        assert hasattr(config, "STOP_KEY")

    def test_config_can_be_modified(self):
        """Test that config values can be modified at runtime."""
        original_cps = config.CPS
        config.CPS = 20
        assert config.CPS == 20
        # Restore original value
        config.CPS = original_cps
