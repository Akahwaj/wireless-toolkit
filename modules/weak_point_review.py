def run_weak_point_review():
    print("\n[Weak Point Review]")
    print("Choose what you want to review:")
    print("1. Wireless encryption")
    print("2. Signal strength")
    print("3. Environment approval")
    print("4. Back")

    choice = input("\nChoose an option (1-4): ").strip()

    if choice == "1":
        encryption = input("Enter encryption type (WPA3/WPA2/Open/Unknown): ").strip().lower()

        print("\nReview Result:")
        if encryption == "wpa3":
            print("Risk: Low")
            print("Finding: Strong wireless encryption detected.")
            print("Recommendation: Continue using strong encryption and review configuration regularly.")
        elif encryption == "wpa2":
            print("Risk: Medium")
            print("Finding: WPA2 detected.")
            print("Recommendation: WPA2 is still widely used, but WPA3 is stronger if supported.")
        elif encryption == "open":
            print("Risk: High")
            print("Finding: Open wireless network detected.")
            print("Recommendation: Avoid open wireless access unless it is intentionally designed and isolated.")
        else:
            print("Risk: Medium")
            print("Finding: Unknown encryption type.")
            print("Recommendation: Confirm the wireless security settings.")

    elif choice == "2":
        try:
            signal = int(input("Enter signal strength in dBm (example: -67): ").strip())
        except ValueError:
            print("Invalid signal strength.")
            return

        print("\nReview Result:")
        if signal >= -50:
            print("Risk: Low")
            print("Finding: Excellent signal strength.")
            print("Recommendation: No immediate action needed.")
        elif signal >= -67:
            print("Risk: Low")
            print("Finding: Good signal strength.")
            print("Recommendation: Continue monitoring signal quality.")
        elif signal >= -75:
            print("Risk: Medium")
            print("Finding: Fair signal strength.")
            print("Recommendation: Review placement and coverage for better consistency.")
        else:
            print("Risk: High")
            print("Finding: Weak signal strength.")
            print("Recommendation: Investigate wireless coverage and connectivity issues.")

    elif choice == "3":
        approved = input("Was environment approval confirmed? (yes/no): ").strip().lower()
        print("\nReview Result:")
        if approved in {"yes", "y"}:
            print("Risk: Low")
            print("Finding: Environment approval confirmed.")
            print("Recommendation: Proceed within documented scope.")
        else:
            print("Risk: High")
            print("Finding: Environment approval not confirmed.")
            print("Recommendation: Stop and verify authorization before continuing.")

    elif choice == "4":
        return
    else:
        print("\nInvalid choice.")
