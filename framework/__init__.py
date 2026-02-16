"""
Regression Testing Framework
A comprehensive testing framework for validating system integrations and component interactions.
"""

__version__ = "1.0.0"
__author__ = "Software Engineer Intern"

from .test_base import TestBase
from .fixtures import TestFixtures
from .report_generator import ReportGenerator

__all__ = ["TestBase", "TestFixtures", "ReportGenerator"]
