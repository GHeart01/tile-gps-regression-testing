"""
Test fixtures and mock data for regression tests.
"""

import json
from typing import Any, Dict, List
from datetime import datetime


class TestFixtures:
    """Provides test data and fixture utilities."""

    @staticmethod
    def get_sample_tile_data() -> Dict[str, Any]:
        """Get sample TILE module data."""
        return {
            "module_id": "TILE_001",
            "name": "Tile Test Module",
            "version": "2.1.0",
            "status": "active",
            "timestamp": datetime.now().isoformat(),
            "data": {
                "grid_size": 1024,
                "resolution": 0.1,
                "regions": 4,
                "quality_metrics": {
                    "coverage": 99.5,
                    "accuracy": 98.7,
                }
            }
        }

    @staticmethod
    def get_sample_emquest_gps_data() -> Dict[str, Any]:
        """Get sample EMQuest GPS module data."""
        return {
            "device_id": "EMQ_GPS_001",
            "location": {
                "latitude": 30.2672,
                "longitude": -97.7431,  # Cedar Park, TX area
                "accuracy": 5.0,
                "altitude": 250.5
            },
            "signal_strength": 85,
            "satellites": 12,
            "fix_quality": "RTK Fixed",
            "timestamp": datetime.now().isoformat()
        }

    @staticmethod
    def get_sample_spectra_python_integration() -> Dict[str, Any]:
        """Get sample Spectra Python integration test data."""
        return {
            "integration_id": "SPEC_PY_001",
            "system": "Spectra",
            "language": "Python",
            "version": "3.9+",
            "modules": ["core", "analytics", "visualization"],
            "status": "initialized",
            "configuration": {
                "timeout": 30,
                "retry_attempts": 3,
                "log_level": "INFO"
            },
            "timestamp": datetime.now().isoformat()
        }

    @staticmethod
    def get_sample_aurora_data() -> Dict[str, Any]:
        """Get sample Aurora system data."""
        return {
            "system_id": "AURORA_001",
            "name": "Aurora Integration Test",
            "components": ["core", "services", "analytics"],
            "status": "operational",
            "uptime_seconds": 3600,
            "metrics": {
                "cpu_usage": 45.2,
                "memory_usage": 62.1,
                "network_latency": 12.5
            },
            "timestamp": datetime.now().isoformat()
        }

    @staticmethod
    def create_mock_response(success: bool, data: Any = None, 
                           error: str = "") -> Dict[str, Any]:
        """Create a standard mock response."""
        return {
            "success": success,
            "data": data,
            "error": error,
            "timestamp": datetime.now().isoformat()
        }

    @staticmethod
    def create_test_matrix(test_cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create parameterized test matrix."""
        return test_cases
