from modules.safety_checks import authorized_use_check
from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.notes_helper import create_assessment_note
from modules.report_generator import generate_report
from integrations.platform_check import show_platform_support


def show_advanced_menu():
    print("\n================================")
    print("        ADVANCED MODE")
    print("================================")
    print("1. Safety Check")
    print("2. Wi-Fi Audit")
    print("3. Signal Analysis")
    print("4. Create Assessment Notes")
    print("5. Generate Report")
    print("6. Platform Support Info")
    print("7. Back to Main Menu")


def run_advanced_mode():
    while True:
        show_advanced_menu()
        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            authorized_use_check()
        elif choice == "2":
            run_wifi_audit()
        elif choice == "3":
            run_signal_analysis()
        elif choice == "4":
            create_assessment_note()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            show_platform_support()
        elif choice == "7":
            break
        else:
            print("\nInvalid choice.")
