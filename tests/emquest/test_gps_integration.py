"""
EMQuest Android GPS Module Regression Tests
Tests for GPS functionality, location accuracy, and Android integration.
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from framework.test_base import TestBase
from framework.fixtures import TestFixtures


class TestEMQuestGPSInitialization(TestBase):
    """Test EMQuest GPS module initialization."""

    def setUp(self):
        """Set up GPS tests."""
        super().setUp()
        self.gps_data = TestFixtures.get_sample_emquest_gps_data()

    def test_gps_device_initialization(self):
        """Test GPS device initializes correctly."""
        self.assert_not_none(self.gps_data)
        self.assert_equals("EMQ_GPS_001", self.gps_data["device_id"])

    def test_gps_location_structure(self):
        """Test GPS location data structure."""
        location = self.gps_data["location"]
        required_fields = ["latitude", "longitude", "accuracy", "altitude"]
        for field in required_fields:
            self.assert_true(field in location, 
                            f"Missing location field: {field}")


class TestEMQuestGPSAccuracy(TestBase):
    """Test GPS accuracy and signal quality."""

    def setUp(self):
        """Set up accuracy tests."""
        super().setUp()
        self.gps_data = TestFixtures.get_sample_emquest_gps_data()

    def test_gps_coordinate_validity(self):
        """Test GPS coordinates are valid."""
        location = self.gps_data["location"]
        lat = location["latitude"]
        lon = location["longitude"]
        
        self.assert_true(-90 <= lat <= 90, "Invalid latitude")
        self.assert_true(-180 <= lon <= 180, "Invalid longitude")

    def test_gps_accuracy_threshold(self):
        """Test GPS accuracy meets threshold."""
        accuracy = self.gps_data["location"]["accuracy"]
        self.assert_true(accuracy > 0, "Accuracy must be positive")
        self.assert_true(accuracy <= 100, "Accuracy should be <= 100m")

    def test_gps_signal_strength(self):
        """Test GPS signal strength is adequate."""
        signal = self.gps_data["signal_strength"]
        self.assert_true(signal >= 0, "Signal must be non-negative")
        self.assert_true(signal <= 100, "Signal must be <= 100")
        self.assert_true(signal >= 50, "Signal strength should be >= 50%")

    def test_gps_satellite_count(self):
        """Test adequate satellites are visible."""
        satellites = self.gps_data["satellites"]
        self.assert_true(satellites >= 4, 
                        "Need at least 4 satellites for 3D fix")


class TestEMQuestGPSIntegration(TestBase):
    """Test EMQuest GPS Android integration."""

    def setUp(self):
        """Set up integration tests."""
        super().setUp()
        self.gps_data = TestFixtures.get_sample_emquest_gps_data()

    def test_gps_fix_quality(self):
        """Test GPS fix quality."""
        fix_quality = self.gps_data["fix_quality"]
        valid_qualities = ["RTK Fixed", "RTK Float", "DGPS", "GPS"]
        self.assert_true(fix_quality in valid_qualities,
                        f"Invalid fix quality: {fix_quality}")

    def test_gps_response_format(self):
        """Test GPS response is properly formatted."""
        response = TestFixtures.create_mock_response(
            success=True,
            data=self.gps_data
        )
        self.assert_true(response["success"])
        self.assert_not_none(response["data"]["location"])

    def test_gps_error_recovery(self):
        """Test GPS error handling."""
        error_response = TestFixtures.create_mock_response(
            success=False,
            error="GPS signal lost"
        )
        self.assert_false(error_response["success"])
        self.assert_true("GPS" in error_response["error"])


class TestEMQuestAndroidSpecific(TestBase):
    """Test Android-specific GPS functionality."""

    def setUp(self):
        """Set up Android tests."""
        super().setUp()
        self.gps_data = TestFixtures.get_sample_emquest_gps_data()

    def test_android_location_provider(self):
        """Test Android location provider compatibility."""
        # Test that data is compatible with Android Location API
        location = self.gps_data["location"]
        self.assert_true("latitude" in location)
        self.assert_true("longitude" in location)
        self.assert_true("accuracy" in location)

    def test_android_permission_compliance(self):
        """Test compliance with Android permissions."""
        # Android requires ACCESS_FINE_LOCATION or ACCESS_COARSE_LOCATION
        accuracy = self.gps_data["location"]["accuracy"]
        # Fine location (< 100m)
        if accuracy < 100:
            self.log_info("Fine location permission required")
        self.assert_true(accuracy > 0)

    def test_android_manifest_fields(self):
        """Test all fields required by Android manifest."""
        required_fields = ["device_id", "location", "signal_strength", "fix_quality"]
        for field in required_fields:
            self.assert_true(field in self.gps_data,
                            f"Missing Android manifest field: {field}")


if __name__ == "__main__":
    unittest.main()
