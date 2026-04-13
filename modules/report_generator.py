from datetime import datetime
from pathlib import Path
from core.session_store import load_session


def generate_report():
    print("\n[Report Generator]")
    project_name = input("Enter project name: ").strip()
    assessor = input("Enter your name: ").strip()
    environment = input("Enter environment name: ").strip()
    summary = input("Enter short summary: ").strip()
    report_title = input("Enter report title: ").strip() or "Client Security Assessment Report"

    session = load_session()
    findings = session.get("findings", [])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines = [
        report_title,
        "=" * 40,
        f"Project: {project_name}",
        f"Assessor: {assessor}",
        f"Environment: {environment}",
        f"Date: {timestamp}",
        "",
        "Executive Summary",
        "-" * 20,
        summary,
        "",
        "Findings",
        "-" * 20,
    ]

    if findings:
        for i, f in enumerate(findings, 1):
            report_lines.extend([
                f"{i}. {f['title']}",
                f"   Severity: {f['severity']}",
                f"   Details: {f['details']}",
                f"   Recommendation: {f['recommendation']}",
                "",
            ])
    else:
        report_lines.append("No findings collected yet.")
        report_lines.append("")

    report_lines.extend([
        "Next Steps",
        "-" * 20,
        "1. Review findings",
        "2. Assign remediation owners",
        "3. Revalidate after fixes",
        "",
    ])

    report_text = "\n".join(report_lines)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path.write_text(report_text, encoding="utf-8")

    print("\nReport created successfully.")
    print(f"Saved to: {file_path}")
    print("\nPreview:\n")
    print(report_text)