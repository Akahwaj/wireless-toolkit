"""
Assessment notes module for the Wireless Toolkit.

Generates a pre-filled plain-text notes template for documenting wireless
assessment environments and saves it to the ``output/`` directory.
"""

from datetime import datetime
from pathlib import Path


def create_assessment_note() -> None:
    """Create a timestamped assessment notes template file.

    Writes a blank assessment notes template to
    ``output/assessment_notes_<YYYY-MM-DD_HH-MM-SS>.txt``.  The output
    directory is created automatically if it does not exist.

    The template includes fields for:
        - Environment description
        - Owner and contact person
        - Access method and approval details
        - Allowed and disallowed actions
        - Date and extra notes

    Returns:
        None

    Example::

        >>> create_assessment_note()
        Assessment notes template created: output/assessment_notes_2024-01-15_10-30-00.txt
    """
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = output_dir / f"assessment_notes_{timestamp}.txt"

    template = """Assessment Notes

Environment:
Owner:
Access method:
Type: Lab / Training / Test / Production
Approved by:
Allowed actions:
Not allowed:
Date:
Contact person:
Extra notes:
"""

    file_path.write_text(template, encoding="utf-8")
    print(f"\nAssessment notes template created: {file_path}")