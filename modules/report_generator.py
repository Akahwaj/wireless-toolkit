from datetime import datetime
from pathlib import Path


def generate_report():
    print("\n[Report Generator]")
    project_name = input("Enter project name: ").strip()
    assessor = input("Enter your name: ").strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""Aegis Toolkit Report
=========================
Project: {project_name}
Assessor: {assessor}
Date: {timestamp}

Summary:
Wireless review completed.

Notes:
- Review collected information carefully
- Confirm environment scope before any further steps
- Save additional observations in assessment notes
"""

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / "report.txt"
    file_path.write_text(report, encoding="utf-8")

    print("\nReport")
    print("=" * 25)
    print(report)
    print(f"Saved to: {file_path}")