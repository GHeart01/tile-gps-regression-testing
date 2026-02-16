"""
Test report generation and analysis utilities.
"""

import json
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path


class ReportGenerator:
    """Generates test reports and metrics."""

    def __init__(self, output_dir: str = "reports"):
        """Initialize report generator."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.test_results: List[Dict[str, Any]] = []

    def add_test_result(self, test_name: str, passed: bool, 
                       duration: float, error: str = ""):
        """Record a test result."""
        result = {
            "test_name": test_name,
            "passed": passed,
            "duration": duration,
            "error": error,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)

    def generate_summary(self) -> Dict[str, Any]:
        """Generate test summary."""
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r["passed"])
        failed = total - passed
        total_duration = sum(r["duration"] for r in self.test_results)

        return {
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": (passed / total * 100) if total > 0 else 0,
            "total_duration": total_duration,
            "timestamp": datetime.now().isoformat()
        }

    def save_json_report(self, filename: str = "test_report.json"):
        """Save report as JSON."""
        report = {
            "summary": self.generate_summary(),
            "results": self.test_results
        }
        output_path = self.output_dir / filename
        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)
        return output_path

    def save_html_report(self, filename: str = "test_report.html"):
        """Save report as HTML."""
        summary = self.generate_summary()
        html_content = self._generate_html(summary)
        output_path = self.output_dir / filename
        with open(output_path, "w") as f:
            f.write(html_content)
        return output_path

    def _generate_html(self, summary: Dict[str, Any]) -> str:
        """Generate HTML report content."""
        pass_rate = summary["pass_rate"]
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Regression Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .summary {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
                .passed {{ color: green; }}
                .failed {{ color: red; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
                th {{ background-color: #4CAF50; color: white; }}
            </style>
        </head>
        <body>
            <h1>Regression Test Report</h1>
            <div class="summary">
                <h2>Summary</h2>
                <p>Total Tests: {summary["total_tests"]}</p>
                <p class="passed">Passed: {summary["passed"]}</p>
                <p class="failed">Failed: {summary["failed"]}</p>
                <p>Pass Rate: {pass_rate:.1f}%</p>
                <p>Total Duration: {summary["total_duration"]:.2f}s</p>
            </div>
            <h2>Test Results</h2>
            <table>
                <tr>
                    <th>Test Name</th>
                    <th>Status</th>
                    <th>Duration (s)</th>
                </tr>
        """
        for result in self.test_results:
            status = "PASSED" if result["passed"] else "FAILED"
            status_class = "passed" if result["passed"] else "failed"
            html += f"""
                <tr>
                    <td>{result["test_name"]}</td>
                    <td class="{status_class}">{status}</td>
                    <td>{result["duration"]:.3f}</td>
                </tr>
            """
        html += """
            </table>
        </body>
        </html>
        """
        return html
