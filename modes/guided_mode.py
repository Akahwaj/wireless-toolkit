from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from modules.teach_helper import explain_topic


def run_guided_mode():
    print("\n================================")
    print("        GUIDED MODE")
    print("================================")
    print("1. Help Me Check Wireless")
    print("2. Help Me Check Signal")
    print("3. Confirm My Environment")
    print("4. Create Report")
    print("5. Create Notes")
    print("6. Learn What These Tools Do")
    print("7. Back")

    choice = input("\nChoose an option (1-7): ").strip()

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
        print("\nTopics:")
        print("1. Wireless Check")
        print("2. Signal Check")
        print("3. Safety Check")
        print("4. Report")
        print("5. Notes")

        topic_choice = input("\nChoose a topic (1-5): ").strip()
        topic_map = {
            "1": "wifi",
            "2": "signal",
            "3": "safety",
            "4": "report",
            "5": "notes",
        }
        explain_topic(topic_map.get(topic_choice, ""))
    elif choice == "7":
        return
    else:
        print("\nInvalid choice.")
