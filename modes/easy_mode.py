from modules.safety_checks import authorized_use_check
from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.report_generator import generate_report


def run_easy_mode():
    print("\n================================")
    print("         EASY MODE")
    print("================================")
    print("This mode walks you through the")
    print("most common wireless review steps.")

    if not authorized_use_check():
        return

    run_wifi_audit()
    run_signal_analysis()

    save = input("\nWould you like to generate a report? (y/n): ").strip().lower()
    if save == "y":
        generate_report()
