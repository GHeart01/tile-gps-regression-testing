#!/bin/bash
# Quick commands for running the regression testing project

echo "Regression Testing Framework - Quick Commands"
echo "=============================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setup & Installation:${NC}"
echo "  source venv/bin/activate          # Activate virtual environment"
echo "  python3 -m pip install -r requirements.txt  # Install dependencies"
echo ""

echo -e "${BLUE}Running Tests:${NC}"
echo "  pytest tests/ -v                  # Run all 52 tests"
echo "  pytest tests/tile/ -v             # Run TILE module tests"
echo "  pytest tests/emquest/ -v          # Run EMQuest GPS tests"
echo "  pytest tests/spectra/ -v          # Run Spectra Python tests"
echo "  pytest tests/aurora/ -v           # Run Aurora system tests"
echo ""

echo -e "${BLUE}Test Filtering:${NC}"
echo "  pytest tests/ -k 'initialization' # Run tests matching pattern"
echo "  pytest tests/ -k 'gps'            # Run GPS-related tests"
echo "  pytest tests/ -k 'accuracy'       # Run accuracy tests"
echo ""

echo -e "${BLUE}Coverage Reports:${NC}"
echo "  pytest tests/ --cov=framework --cov-report=html"
echo "  # Then open htmlcov/index.html in browser"
echo ""

echo -e "${BLUE}Specific Test Classes:${NC}"
echo "  pytest tests/tile/test_tile_core.py::TestTILEInitialization -v"
echo "  pytest tests/emquest/test_gps_integration.py::TestEMQuestGPSAccuracy -v"
echo ""

echo -e "${BLUE}Project Information:${NC}"
echo "  cat README.md                     # View full documentation"
echo "  cat INTERVIEW_GUIDE.md            # View interview preparation"
echo "  cat PROJECT_STATS.md              # View project statistics"
echo "  ls -la                            # Show project structure"
echo ""

echo -e "${GREEN}✅ All commands ready to run!${NC}"
