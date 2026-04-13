import re


def _is_valid_mac(mac: str) -> bool:
    pattern = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")
    return bool(pattern.match(mac))


def run_mac_checker():
    print("\n[MAC Address Checker]")
    print("MAC addresses identify network interfaces. Spoofing or reviewing MAC addresses")
    print("is useful for privacy analysis and authorized network assessments.\n")

    mac = input("Enter the MAC address to check (format: AA:BB:CC:DD:EE:FF): ").strip()

    if not _is_valid_mac(mac):
        print("\nInvalid MAC address format. Expected format: AA:BB:CC:DD:EE:FF")
        return

    parts = mac.split(":")
    oui = ":".join(parts[:3]).upper()
    first_octet_bits = int(parts[0], 16)
    is_multicast = bool(first_octet_bits & 0x01)
    is_locally_administered = bool(first_octet_bits & 0x02)

    print(f"\nMAC Address: {mac.upper()}")
    print(f"OUI (Manufacturer prefix): {oui}")
    print(f"Multicast bit set: {is_multicast}")
    print(f"Locally administered (possibly spoofed): {is_locally_administered}")

    print("\nAnalysis:")
    if is_locally_administered:
        print("- Risk: Medium")
        print("- Finding: Locally administered bit is set. This MAC may be spoofed or randomized.")
        print("- Recommendation: Verify whether this is an expected privacy feature or an anomaly.")
    else:
        print("- Risk: Low")
        print("- Finding: Globally unique MAC address (manufacturer-assigned OUI).")
        print("- Recommendation: No immediate concern. Monitor for unexpected MAC changes.")

    if is_multicast:
        print("- Additional finding: Multicast bit is set. This is unusual for a device MAC address.")

    print("\nTo change a MAC address on Linux (authorized environments only):")
    print("  sudo ip link set <interface> down")
    print("  sudo ip link set <interface> address <new_mac>")
    print("  sudo ip link set <interface> up")
    print("\nNote: MAC changes should only be performed on interfaces you are authorized to manage.")
