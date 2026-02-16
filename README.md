# Regression Testing Framework

A comprehensive regression testing framework designed for validating complex system integrations across multiple modules including TILE, EMQuest, Spectra, and Aurora systems.

## Overview

This project demonstrates professional testing practices including:
- **Structured test framework** with base classes and fixtures
- **25+ regression tests** across four major system modules
- **Python test examples** for TILE and Spectra integration
- **Comprehensive documentation** and CI/CD setup
- **Report generation** for test results and metrics


```

## Features

### TILE Module Tests
- Module initialization and configuration
- Data processing and grid validation
- Quality metrics verification (coverage, accuracy)
- Python serialization and validation examples

### EMQuest GPS Tests
- GPS device initialization
- Location accuracy validation
- Signal strength monitoring
- Android integration testing
- RTK/DGPS fix quality verification

### Spectra Python Integration Tests
- Python module initialization (3.9+)
- Ancillary state management
- Configuration validation
- Data persistence testing
- Integration error handling

### Aurora System Tests
- System initialization and status
- Performance metrics (CPU, memory, network)
- Component integration verification
- Health monitoring and recovery

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd RegressionTesting
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest tests/
```

### Run specific test module:
```bash
# TILE tests
pytest tests/tile/ -v

# EMQuest tests
pytest tests/emquest/ -v

# Spectra tests
pytest tests/spectra/ -v

# Aurora tests
pytest tests/aurora/ -v
```

### Run with coverage report:
```bash
pytest tests/ --cov=framework --cov-report=html
```

### Run specific test class:
```bash
pytest tests/tile/test_tile_core.py::TestTILEInitialization -v
```

### Run tests matching a pattern:
```bash
pytest tests/ -k "accuracy" -v
```

## Test Coverage

The framework includes:
- **30+ test cases** covering all major system modules
- **Unit tests** for individual components
- **Integration tests** for system interactions
- **Error handling** and recovery scenarios
- **Data validation** and serialization tests

## Key Testing Capabilities

### 1. Test Framework (`framework/`)
- `TestBase`: Base class providing logging, assertions, and utilities
- `TestFixtures`: Mock data generators for all system modules
- `ReportGenerator`: HTML and JSON test report generation

### 2. Test Utilities
- Custom assertion methods with detailed messages
- Structured logging for test execution
- Mock response creation for integration testing
- Parameterized test matrix support

### 3. Python Integration
- Module import validation
- JSON serialization/deserialization
- Data structure validation
- Configuration management

## CI/CD Integration

The project includes GitHub Actions workflow (`.github/workflows/tests.yml`) that:
- Runs tests on Python 3.9, 3.10, and 3.11
- Generates coverage reports
- Uploads results to Codecov
- Validates on push and pull requests

## Configuration

### pytest.ini
Configures:
- Test discovery patterns
- Verbose output
- Coverage reporting
- Custom markers for test categorization

### requirements.txt
Core dependencies:
- `pytest`: Test framework
- `coverage`: Code coverage measurement
- `pytest-cov`: Coverage plugin
- `pytest-html`: HTML report generation

## Development Workflow

### Adding New Tests

1. Create a test file in the appropriate module directory
2. Extend `TestBase` class
3. Use `TestFixtures` for mock data
4. Follow naming convention: `test_*.py`

Example:
```python
from framework.test_base import TestBase
from framework.fixtures import TestFixtures

class TestMyFeature(TestBase):
    def setUp(self):
        super().setUp()
        self.data = TestFixtures.get_sample_tile_data()
    
    def test_my_functionality(self):
        self.assert_not_none(self.data)
        self.assert_equals("expected", "actual")
```

### Running Tests Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `pytest tests/ -v`
3. View coverage: Open `htmlcov/index.html` in browser

## Report Generation

Test reports are automatically generated:
- **HTML Report**: `reports/test_report.html`
- **JSON Report**: `reports/test_report.json`
- **Coverage Report**: `htmlcov/index.html`



