from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from integrations.platform_check import show_platform_support


def show_advanced_menu():
    print("\n================================")
    print("       ADVANCED MODE")
    print("================================")
    print("1. Run WiFi Audit")
    print("2. Run Signal Analysis")
    print("3. Run Safety Check")
    print("4. Generate Report")
    print("5. Create Notes")
    print("6. Check Platform Support")
    print("7. Back")


def run_advanced_mode():
    while True:
        show_advanced_menu()
        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            run_wifi_audit()
        elif choice == "2":
            run_signal_analysis()
        elif choice == "3":
            authorized_use_check()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            create_assessment_note()
        elif choice == "6":
            show_platform_support()
        elif choice == "7":
            return
        else:
            print("\nInvalid choice.")
