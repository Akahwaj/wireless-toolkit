"""
Report generation module for the Wireless Toolkit.

Creates a plain-text assessment report and saves it to the ``output/``
directory (created automatically if it does not exist).
"""

from datetime import datetime
from pathlib import Path


def generate_report() -> None:
    """Generate and save a plain-text wireless assessment report.

    Prompts the user for a project name and assessor name, then writes a
    timestamped report to ``output/report.txt``, overwriting any previous
    file with the same name.  The report is also printed to stdout.

    The output directory (``output/``) is created automatically relative
    to the current working directory if it does not already exist.

    Returns:
        None

    Example::

        >>> generate_report()
        [Report Generator]
        Enter project name: LabAudit
        Enter your name: Alice
        ...
        Saved to: output/report.txt
    """
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