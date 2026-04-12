def run_wifi_audit():
    print("\n[Wi-Fi Audit]")
    ssid = input("Enter SSID name: ").strip()
    encryption = input("Enter encryption type (WPA2/WPA3/Open): ").strip()

    print("\nAudit Summary:")
    print(f"- SSID: {ssid}")
    print(f"- Encryption: {encryption}")

    if encryption.lower() == "open":
        print("- Review: Open networks should only be used intentionally.")
    elif encryption.lower() == "wpa2":
        print("- WPA2 is good, WPA3 is better.")
    elif encryption.lower() == "wpa3":
        print("- Strong security (WPA3).")
    else:
        print("- Unknown encryption.")