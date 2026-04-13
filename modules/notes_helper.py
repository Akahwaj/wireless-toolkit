from datetime import datetime
from pathlib import Path


def create_assessment_note():
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
