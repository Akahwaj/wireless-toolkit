import shutil


def run_interface_helper():
    print("\n[Wireless Interface Helper]")
    print("Wireless interfaces need to be in the correct mode for different audit tasks.")
    print("This guide reviews interface requirements and checks for installed tools.\n")

    interface = input("Enter your wireless interface name (example: wlan0): ").strip()

    print("\nInterface Guide:")
    print(f"- Interface name: {interface if interface else 'Not provided'}")

    print("\nCommon interface modes:")
    print("  managed   - Normal client mode (connecting to access points)")
    print("  monitor   - Passive capture mode (required for packet capture and handshake capture)")
    print("  master    - Access point mode (used by hostapd)")

    print("\nUseful commands (authorized environments only):")
    print("  Check current mode:")
    print(f"    iwconfig {interface if interface else '<interface>'}")
    print("  Enable monitor mode:")
    print(f"    sudo airmon-ng start {interface if interface else '<interface>'}")
    print("  Disable monitor mode:")
    print(f"    sudo airmon-ng stop {interface if interface else '<interface>mon'}")
    print("  Bring interface up or down:")
    print(f"    sudo ip link set {interface if interface else '<interface>'} up")
    print(f"    sudo ip link set {interface if interface else '<interface>'} down")

    print("\nTool availability check:")
    tools = {
        "airmon-ng": "Monitor mode management (aircrack-ng suite)",
        "airodump-ng": "Packet capture and network discovery (aircrack-ng suite)",
        "aireplay-ng": "Packet injection and deauth (aircrack-ng suite)",
        "aircrack-ng": "Handshake and key cracking (aircrack-ng suite)",
        "iwconfig": "Wireless interface configuration",
        "iw": "Modern wireless interface management",
    }

    for tool, description in tools.items():
        installed = shutil.which(tool) is not None
        status = "Installed" if installed else "Not found"
        print(f"  {tool:<15} {status:<12} ({description})")

    print("\nNote: Only modify interfaces on systems you are authorized to manage.")
