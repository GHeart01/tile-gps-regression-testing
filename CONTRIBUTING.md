# Contributing to Regression Testing Framework

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Install dependencies: `pip install -r requirements.txt`

## Development Guidelines

### Code Style
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Keep lines under 100 characters

### Testing Requirements
- Write tests for all new features
- Ensure test names are descriptive
- Use `TestBase` for all test classes
- Use `TestFixtures` for mock data
- Aim for >80% code coverage

### Commit Messages
Use clear, concise commit messages:
```
Add: New regression test for feature X
Fix: Corrected test assertion in module Y
Update: Improved documentation for setup
Refactor: Simplified test fixture generation
```

## Test Writing Guidelines

### Structure
```python
from framework.test_base import TestBase
from framework.fixtures import TestFixtures

class TestMyFeature(TestBase):
    def setUp(self):
        super().setUp()
        self.data = TestFixtures.get_sample_data()
    
    def test_specific_behavior(self):
        """Test description."""
        # Arrange
        expected = "value"
        
        # Act
        actual = self.data.get("key")
        
        # Assert
        self.assert_equals(expected, actual)
```

### Best Practices
- One assertion per test method when possible
- Use descriptive test names starting with `test_`
- Include docstrings explaining what is tested
- Use appropriate assertion methods from `TestBase`
- Mock external dependencies

## Creating Pull Requests

1. Push to your feature branch
2. Create a pull request with clear description
3. Reference related issues
4. Ensure all tests pass
5. Request review from team members

### PR Template
```
## Description
Brief description of changes

## Related Issue
Closes #123

## Changes Made
- Change 1
- Change 2

## Testing
- [ ] Tests added
- [ ] Tests passing
- [ ] Coverage maintained
```

## Adding New Test Modules

When adding tests for a new system:

1. Create directory: `tests/new_module/`
2. Create `__init__.py`
3. Create `test_new_module_core.py`
4. Update fixtures in `framework/fixtures.py`
5. Update README.md with module description
6. Add GitHub workflow if needed

## Running Tests Locally

```bash
# All tests
pytest tests/ -v

# Specific module
pytest tests/tile/ -v

# With coverage
pytest tests/ --cov=framework --cov-report=html

# Specific test class
pytest tests/tile/test_tile_core.py::TestTILEInitialization -v

# Tests matching pattern
pytest tests/ -k "accuracy" -v
```

## Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions/classes
- Comment complex logic
- Update pytest.ini for new markers
- Add examples for new features

## Code Review Process

- Reviewers will check code quality and test coverage
- Address feedback promptly
- Respond to all comments before merging
- Squash commits if requested

## Reporting Issues

Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Python and pytest versions
- Relevant test output

## Questions?

Feel free to open an issue for:
- Questions about testing approach
- Clarification on guidelines
- Feature requests
- Bug reports

---

Happy testing! 🧪
