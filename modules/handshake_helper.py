def run_handshake_helper():
    print("\n[Handshake Capture Helper]")
    print("A WPA/WPA2 handshake is captured when a client connects or reconnects to an access point.")
    print("This guide reviews your handshake capture setup and helps identify gaps.\n")

    interface = input("Enter your wireless interface name (example: wlan0): ").strip()
    monitor_mode = input("Is monitor mode enabled on this interface? (yes/no): ").strip().lower()

    print("\nHandshake Capture Review:")
    print(f"- Interface: {interface if interface else 'Not provided'}")

    if monitor_mode in {"yes", "y"}:
        print("- Monitor mode: Enabled")
        print("- Status: Ready for handshake capture workflow.")
        print("\nTypical capture workflow (authorized environments only):")
        print("  1. Run airodump-ng to discover networks and note the BSSID and channel.")
        print("  2. Focus airodump-ng on the target BSSID and channel to capture traffic.")
        print("  3. Wait for a client to connect, or send a deauth frame to force reconnection.")
        print("  4. Confirm the handshake appears in the airodump-ng output.")
        print("  5. Use aircrack-ng with a wordlist to test captured handshake offline.")
        print("\nTools referenced: airodump-ng, aireplay-ng, aircrack-ng (part of aircrack-ng suite).")
    elif monitor_mode in {"no", "n"}:
        print("- Monitor mode: Disabled")
        print("- Status: Monitor mode must be enabled before capturing handshakes.")
        print("\nTo enable monitor mode (authorized environments only):")
        print(f"  sudo airmon-ng start {interface if interface else '<interface>'}")
        print("  This typically creates a new interface such as wlan0mon.")
    else:
        print("- Monitor mode: Unknown")
        print("- Status: Confirm that monitor mode is enabled before proceeding.")

    print("\nNote: Handshake capture should only be performed on networks you are authorized to test.")
