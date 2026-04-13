from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from modules.teach_helper import explain_topic
from modules.wps_audit import run_wps_audit
from modules.handshake_helper import run_handshake_helper
from modules.mac_checker import run_mac_checker
from modules.interface_helper import run_interface_helper


def run_guided_mode():
    print("\n================================")
    print("        GUIDED MODE")
    print("================================")
    print("1. Help Me Check Wireless")
    print("2. Help Me Check Signal")
    print("3. Confirm My Environment")
    print("4. Create Report")
    print("5. Create Notes")
    print("6. WPS Audit")
    print("7. Handshake Helper")
    print("8. MAC Address Checker")
    print("9. Interface Helper")
    print("10. Learn What These Tools Do")
    print("11. Back")

    choice = input("\nChoose an option (1-11): ").strip()

    if choice == "1":
        print("\nThis will guide you through a basic wireless review.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_wifi_audit()
    elif choice == "2":
        print("\nThis will guide you through a basic signal review.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_signal_analysis()
    elif choice == "3":
        authorized_use_check()
    elif choice == "4":
        print("\nThis will create a simple report file.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            generate_report()
    elif choice == "5":
        create_assessment_note()
    elif choice == "6":
        print("\nThis will guide you through a WPS vulnerability check.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_wps_audit()
    elif choice == "7":
        print("\nThis will guide you through the WPA/WPA2 handshake capture workflow.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_handshake_helper()
    elif choice == "8":
        print("\nThis will analyze a MAC address and explain spoofing detection.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_mac_checker()
    elif choice == "9":
        print("\nThis will help you manage wireless interfaces and check installed tools.")
        if input("Continue? (y/n): ").strip().lower() == "y":
            run_interface_helper()
    elif choice == "10":
        print("\nTopics:")
        print("1. Wireless Check")
        print("2. Signal Check")
        print("3. Safety Check")
        print("4. Report")
        print("5. Notes")
        print("6. WPS Audit")
        print("7. Handshake Helper")
        print("8. MAC Address Checker")
        print("9. Interface Helper")

        topic_choice = input("\nChoose a topic (1-9): ").strip()
        topic_map = {
            "1": "wifi",
            "2": "signal",
            "3": "safety",
            "4": "report",
            "5": "notes",
            "6": "wps",
            "7": "handshake",
            "8": "mac",
            "9": "interface",
        }
        explain_topic(topic_map.get(topic_choice, ""))
    elif choice == "11":
        return
    else:
        print("\nInvalid choice.")
