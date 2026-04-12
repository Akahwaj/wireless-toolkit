from datetime import datetime
from pathlib import Path


def generate_report():
    print("\n[Report Generator]")
    project_name = input("Enter project name: ").strip()
    assessor = input("Enter your name: ").strip()
    environment = input("Enter environment name: ").strip()
    summary = input("Enter short summary: ").strip()
    report_title = input("Enter report title: ").strip() or "Client Security Assessment Report"
report_lines = [
    report_title,
    findings = []
    while True:
        add_more = input("\nAdd a finding? (y/n): ").strip().lower()
        if add_more != "y":
            break

        title = input("Finding title: ").strip()
        severity = input("Severity (Low/Medium/High): ").strip()
        details = input("Finding details: ").strip()
        recommendation = input("Recommendation: ").strip()

        findings.append({
            "title": title,
            "severity": severity,
            "details": details,
            "recommendation": recommendation,
        })

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
        for index, finding in enumerate(findings, start=1):
            report_lines.extend([
                f"{index}. {finding['title']}",
                f"   Severity: {finding['severity']}",
                f"   Details: {finding['details']}",
                f"   Recommendation: {finding['recommendation']}",
                "",
            ])
    else:
        report_lines.append("No findings entered.\n")

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