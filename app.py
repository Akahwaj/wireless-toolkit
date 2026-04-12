from modules.wifi_audit import run_wifi_audit as wifi_audit_tool
from modules.signal_analysis import run_signal_analysis as signal_analysis_tool
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report as report_generator_tool


def safety_checks_tool():
    print("\n[Safety Checks]")
    allowed = authorized_use_check()

    if allowed:
        print("Authorized use confirmed.")
    else:
        print("Authorization not confirmed. Exiting safety check.")


MENU_ACTIONS = {
    "1": (wifi_audit_tool, "WiFi Audit"),
    "2": (signal_analysis_tool, "Signal Analysis"),
    "3": (safety_checks_tool, "Safety Checks"),
    "4": (report_generator_tool, "Report Generator"),
}


def pause():
    input("\nPress Enter to return to the menu...")


def run_teach_mode():
    print("\n🎓 Teach Mode")
    print("Type what you want to do:")
    print("- wifi")
    print("- signal")
    print("- safety")
    print("- report")

    task = input("\nTeach Mode task: ").strip().lower()

    if "wifi" in task or "audit" in task:
        print("\n[Teach Mode]")
        print("This tool handles WiFi auditing workflows and guided checks.")
        wifi_audit_tool()

    elif "signal" in task:
        print("\n[Teach Mode]")
        print("This tool helps analyze wireless signal conditions and behavior.")
        signal_analysis_tool()

    elif "safety" in task:
        print("\n[Teach Mode]")
        print("This tool checks whether you are operating in an authorized environment.")
        safety_checks_tool()

    elif "report" in task:
        print("\n[Teach Mode]")
        print("This tool generates a simple wireless review report.")
        report_generator_tool()

    else:
        print("\nNo matching teach-mode tool found.")


def run_expert_mode():
    print("\n⚡ Expert Tools")
    print("Type exact tool:")
    print("- wifi")
    print("- signal")
    print("- safety")
    print("- report")

    task = input("\nExpert task: ").strip().lower()

    if task == "wifi":
        wifi_audit_tool()
    elif task == "signal":
        signal_analysis_tool()
    elif task == "safety":
        safety_checks_tool()
    elif task == "report":
        report_generator_tool()
    else:
        print("\nUnknown expert tool.")


def show_menu():
    print("\n📡 Wireless Toolkit - All In One")
    print("====================================")
    for key, (_, description) in MENU_ACTIONS.items():
        print(f"{key}. {description}")
    print("5. Teach Mode")
    print("6. Expert Tools")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-7): ").strip()

        if choice in MENU_ACTIONS:
            try:
                MENU_ACTIONS[choice][0]()
            except Exception as e:
                print(f"\nAn error occurred while running the tool: {e}")
            pause()

        elif choice == "5":
            run_teach_mode()
            pause()

        elif choice == "6":
            run_expert_mode()
            pause()

        elif choice == "7":
            print("\nGoodbye. Stay legal and stay sharp.")
            return

        else:
            print("\nInvalid choice.")
            pause()


if __name__ == "__main__":
    main()