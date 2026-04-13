from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from modules.security_review import run_security_review
from modules.weak_point_review import run_weak_point_review
from modules.wps_audit import run_wps_audit
from modules.handshake_helper import run_handshake_helper
from modules.mac_checker import run_mac_checker
from modules.interface_helper import run_interface_helper
from integrations.platform_check import show_platform_support


def show_advanced_menu():
    print("\n================================")
    print("       ADVANCED MODE")
    print("================================")
    print("1. Run WiFi Audit")
    print("2. Run Signal Analysis")
    print("3. Run Safety Check")
    print("4. Run Weak Point Review")
    print("5. Generate Report")
    print("6. Create Notes")
    print("7. Platform Check")
    print("8. Security Review")
    print("9. WPS Audit")
    print("10. Handshake Helper")
    print("11. MAC Address Checker")
    print("12. Interface Helper")
    print("13. Back")


def run_advanced_mode():
    while True:
        show_advanced_menu()
        choice = input("\nChoose an option (1-13): ").strip()

        if choice == "1":
            run_wifi_audit()
        elif choice == "2":
            run_signal_analysis()
        elif choice == "3":
            authorized_use_check()
        elif choice == "4":
            run_weak_point_review()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            create_assessment_note()
        elif choice == "7":
            show_platform_support()
        elif choice == "8":
            run_security_review()
        elif choice == "9":
            run_wps_audit()
        elif choice == "10":
            run_handshake_helper()
        elif choice == "11":
            run_mac_checker()
        elif choice == "12":
            run_interface_helper()
        elif choice == "13":
            return
        else:
            print("\nInvalid choice.")
