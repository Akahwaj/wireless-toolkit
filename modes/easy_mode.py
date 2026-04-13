from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from modules.wps_audit import run_wps_audit
from modules.handshake_helper import run_handshake_helper


def show_easy_menu():
    print("\n================================")
    print("        EASY MODE")
    print("================================")
    print("1. Run Wireless Check")
    print("2. Run Signal Check")
    print("3. Safety Check")
    print("4. Create Simple Report")
    print("5. Create My Notes")
    print("6. WPS Audit")
    print("7. Handshake Helper")
    print("8. Back")


def run_easy_mode():
    while True:
        show_easy_menu()
        choice = input("\nChoose an option (1-8): ").strip()

        if choice == "1":
            print("\n[Wireless Check]")
            run_wifi_audit()
        elif choice == "2":
            print("\n[Signal Check]")
            run_signal_analysis()
        elif choice == "3":
            print("\n[Safety Check]")
            allowed = authorized_use_check()
            if allowed:
                print("Approved environment confirmed.")
            else:
                print("Approval not confirmed.")
        elif choice == "4":
            print("\n[Simple Report]")
            generate_report()
        elif choice == "5":
            print("\n[Create My Notes]")
            create_assessment_note()
        elif choice == "6":
            run_wps_audit()
        elif choice == "7":
            run_handshake_helper()
        elif choice == "8":
            return
        else:
            print("\nInvalid choice.")
