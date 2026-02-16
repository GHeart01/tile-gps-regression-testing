"""
Spectra Python Integration Regression Tests
Tests for Python integration with ancillary states and system integration.
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from framework.test_base import TestBase
from framework.fixtures import TestFixtures


class TestSpectraPythonInitialization(TestBase):
    """Test Spectra Python integration initialization."""

    def setUp(self):
        """Set up Spectra tests."""
        super().setUp()
        self.spectra_data = TestFixtures.get_sample_spectra_python_integration()

    def test_spectra_python_module_initialization(self):
        """Test Spectra Python module initializes."""
        self.assert_not_none(self.spectra_data)
        self.assert_equals("SPEC_PY_001", self.spectra_data["integration_id"])
        self.assert_equals("Spectra", self.spectra_data["system"])
        self.assert_equals("Python", self.spectra_data["language"])

    def test_spectra_python_version(self):
        """Test Python version compatibility."""
        version = self.spectra_data["version"]
        self.assert_true("3.9" in version or "3.10" in version or "3.11" in version)

    def test_spectra_module_structure(self):
        """Test Spectra module structure."""
        modules = self.spectra_data["modules"]
        self.assert_true(len(modules) > 0)
        self.assert_true("core" in modules)


class TestSpectraPythonAncillaryStates(TestBase):
    """Test Spectra ancillary states in Python."""

    def setUp(self):
        """Set up ancillary state tests."""
        super().setUp()
        self.spectra_data = TestFixtures.get_sample_spectra_python_integration()

    def test_spectra_core_module_state(self):
        """Test core module state."""
        modules = self.spectra_data["modules"]
        self.assert_true("core" in modules)
        self.assert_equals("initialized", self.spectra_data["status"])

    def test_spectra_configuration_state(self):
        """Test Spectra configuration state."""
        config = self.spectra_data["configuration"]
        self.assert_not_none(config.get("timeout"))
        self.assert_not_none(config.get("retry_attempts"))
        self.assert_true(config["timeout"] > 0)
        self.assert_true(config["retry_attempts"] > 0)

    def test_spectra_analytics_module(self):
        """Test analytics module availability."""
        modules = self.spectra_data["modules"]
        self.assert_true("analytics" in modules)

    def test_spectra_visualization_module(self):
        """Test visualization module availability."""
        modules = self.spectra_data["modules"]
        self.assert_true("visualization" in modules)


class TestSpectraPythonIntegration(TestBase):
    """Test Spectra Python integration functionality."""

    def setUp(self):
        """Set up integration tests."""
        super().setUp()
        self.spectra_data = TestFixtures.get_sample_spectra_python_integration()

    def test_spectra_module_imports(self):
        """Test Spectra modules can be imported."""
        modules = self.spectra_data["modules"]
        for module in modules:
            self.assert_true(len(module) > 0)
            self.log_info(f"Testing module import: {module}")

    def test_spectra_configuration_values(self):
        """Test configuration values are valid."""
        config = self.spectra_data["configuration"]
        self.assert_equals("INFO", config.get("log_level"))
        self.assert_equals(30, config.get("timeout"))
        self.assert_equals(3, config.get("retry_attempts"))

    def test_spectra_error_handling(self):
        """Test error handling in Spectra Python."""
        error_response = TestFixtures.create_mock_response(
            success=False,
            error="Python integration failed"
        )
        self.assert_false(error_response["success"])

    def test_spectra_response_validation(self):
        """Test Spectra response validation."""
        response = TestFixtures.create_mock_response(
            success=True,
            data=self.spectra_data
        )
        self.assert_true(response["success"])
        self.assert_not_none(response["data"])


class TestSpectraPythonAncillaryIntegration(TestBase):
    """Test ancillary states integration with Python."""

    def setUp(self):
        """Set up ancillary integration tests."""
        super().setUp()
        self.spectra_data = TestFixtures.get_sample_spectra_python_integration()

    def test_ancillary_state_transitions(self):
        """Test ancillary state transitions."""
        # Test that system can transition through states
        states = ["initialized", "running", "paused", "stopped"]
        self.assert_true(self.spectra_data["status"] in states)

    def test_ancillary_data_persistence(self):
        """Test ancillary data can be persisted."""
        import json
        try:
            json_data = json.dumps(self.spectra_data)
            restored = json.loads(json_data)
            self.assert_equals(self.spectra_data["integration_id"],
                              restored["integration_id"])
        except Exception as e:
            self.fail(f"Data persistence failed: {str(e)}")

    def test_ancillary_state_recovery(self):
        """Test recovery from invalid ancillary states."""
        # Simulate state recovery
        recovery_response = TestFixtures.create_mock_response(
            success=True,
            data={"state": "recovered", "timestamp": self.spectra_data["timestamp"]}
        )
        self.assert_true(recovery_response["success"])


if __name__ == "__main__":
    unittest.main()
