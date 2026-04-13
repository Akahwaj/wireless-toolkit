import platform
import shutil
import sys


def _check_tool(name: str) -> str:
    return "installed" if shutil.which(name) is not None else "not found"


def show_system_info():
    print("\n" + "=" * 60)
    print("              SYSTEM INFORMATION")
    print("=" * 60)

    # OS / Python
    print("\n  [System]")
    print(f"    OS              : {platform.system()} {platform.release()}")
    print(f"    Machine         : {platform.machine()}")
    print(f"    Python version  : {sys.version.split()[0]}")
    print(f"    Platform string : {platform.platform()}")

    # Wireless / capture tools
    print("\n  [Wireless & Capture Tools]")
    tools = [
        ("iw",            "Linux wireless utility"),
        ("iwconfig",      "Legacy wireless config (deprecated)"),
        ("airmon-ng",     "Monitor mode management (aircrack-ng)"),
        ("airodump-ng",   "Passive 802.11 capture (aircrack-ng)"),
        ("tshark",        "CLI packet capture (Wireshark)"),
        ("tcpdump",       "CLI packet capture"),
        ("dumpcap",       "High-performance capture (Wireshark)"),
        ("kismet",        "Passive WLAN discovery"),
        ("nmcli",         "NetworkManager CLI"),
        ("nmap",          "Network mapper"),
    ]
    for tool, description in tools:
        status = _check_tool(tool)
        print(f"    {tool:<15} : {status:<12}  ({description})")

    print()
    print("  Note: This display is informational only.")
    print("  Install tools only in authorized lab environments.")
    input("\nPress Enter to return to the main menu...")
