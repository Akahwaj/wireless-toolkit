from modules.safety_checks import authorized_use_check
from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.notes_helper import create_assessment_note
from modules.report_generator import generate_report
from modules.teach_helper import explain_topic


def run_guided_mode():
    print("\n================================")
    print("         GUIDED MODE")
    print("================================")
    print("This mode explains each step as")
    print("you go through the assessment.")

    explain_topic("safety")
    if not authorized_use_check():
        return

    explain_topic("notes")
    create_assessment_note()

    explain_topic("wifi")
    run_wifi_audit()

    explain_topic("signal")
    run_signal_analysis()

    explain_topic("report")
    save = input("\nWould you like to generate a report? (y/n): ").strip().lower()
    if save == "y":
        generate_report()
