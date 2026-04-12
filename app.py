from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.report_generator import generate_report
from modules.safety_checks import authorized_use_check


def main():
    print("📡 Wireless Toolkit")
    print("=" * 24)

    if not authorized_use_check():
        print("Authorization check failed. Exiting.")
        return

    while True:
        print("\n1. Wi-Fi Audit")
        print("2. Signal Analysis")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            run_wifi_audit()
        elif choice == "2":
            run_signal_analysis()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
