"""
Base test class for all regression tests.
Provides common setup, teardown, and utility methods.
"""

import unittest
import logging
from datetime import datetime
from typing import Any, Dict, Optional


class TestBase(unittest.TestCase):
    """Base class for all regression tests."""

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.info(f"Starting test class: {cls.__name__}")
        cls.test_start_time = datetime.now()

    @classmethod
    def tearDownClass(cls):
        """Tear down test class."""
        test_duration = datetime.now() - cls.test_start_time
        cls.logger.info(
            f"Completed test class: {cls.__name__} "
            f"(Duration: {test_duration.total_seconds():.2f}s)"
        )

    def setUp(self):
        """Set up test method."""
        self.test_id = self.id()
        self.logger.debug(f"Running test: {self.test_id}")

    def tearDown(self):
        """Tear down test method."""
        self.logger.debug(f"Completed test: {self.test_id}")

    def assert_equals(self, expected: Any, actual: Any, message: str = ""):
        """Assert equality with custom message."""
        self.assertEqual(expected, actual, message)

    def assert_not_none(self, value: Any, message: str = ""):
        """Assert value is not None."""
        self.assertIsNotNone(value, message)

    def assert_true(self, condition: bool, message: str = ""):
        """Assert condition is True."""
        self.assertTrue(condition, message)

    def assert_false(self, condition: bool, message: str = ""):
        """Assert condition is False."""
        self.assertFalse(condition, message)

    def log_info(self, message: str):
        """Log info message."""
        self.logger.info(message)

    def log_debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)

    def log_error(self, message: str):
        """Log error message."""
        self.logger.error(message)
