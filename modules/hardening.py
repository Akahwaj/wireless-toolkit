CHECKLIST = [
    {
        "category": "Encryption",
        "items": [
            ("Use WPA3 or WPA2-AES (avoid TKIP, WEP, or Open)", "critical"),
            ("Disable WEP — it is completely broken", "critical"),
            ("Enable AES/CCMP; disable TKIP if possible", "high"),
            ("Use WPA3-SAE on supported hardware for stronger handshake security", "high"),
        ],
    },
    {
        "category": "Authentication",
        "items": [
            ("Use a strong, unique passphrase (min 16 chars, mixed types)", "critical"),
            ("Prefer WPA2/3-Enterprise (802.1X) over PSK for corporate environments", "high"),
            ("Disable WPS (Wi-Fi Protected Setup) — susceptible to brute force", "high"),
            ("Rotate pre-shared keys regularly in high-risk environments", "medium"),
        ],
    },
    {
        "category": "Management Frame Protection",
        "items": [
            ("Enable Protected Management Frames (PMF / 802.11w)", "high"),
            ("Set PMF to 'Required' rather than 'Optional' where supported", "medium"),
        ],
    },
    {
        "category": "Network Segmentation",
        "items": [
            ("Isolate guest Wi-Fi from internal network (separate VLAN)", "high"),
            ("Enable client isolation on guest networks", "high"),
            ("Separate IoT devices onto a dedicated SSID/VLAN", "medium"),
            ("Restrict wireless clients from reaching management interfaces", "high"),
        ],
    },
    {
        "category": "Access Point Configuration",
        "items": [
            ("Change default admin credentials on all access points", "critical"),
            ("Update AP firmware regularly", "high"),
            ("Disable remote management over Wi-Fi; use wired management only", "high"),
            ("Disable unused SSIDs and radios", "medium"),
            ("Set SSID to a non-identifying name (avoid company name, location)", "low"),
            ("Review and minimize SSID broadcast power to reduce unnecessary range", "low"),
        ],
    },
    {
        "category": "Monitoring & Logging",
        "items": [
            ("Enable AP syslog and forward to a central log server", "high"),
            ("Enable WIDS/WIPS (Wireless Intrusion Detection/Prevention) if available", "high"),
            ("Regularly review logs for unexpected clients or association events", "medium"),
            ("Document expected BSSIDs/MACs for your environment", "medium"),
        ],
    },
    {
        "category": "Physical Security",
        "items": [
            ("Physically secure access points to prevent tampering or replacement", "medium"),
            ("Place APs to minimize signal leakage outside the intended area", "medium"),
        ],
    },
    {
        "category": "Client Security",
        "items": [
            ("Disable auto-connect to open or unknown networks on client devices", "high"),
            ("Use a VPN when connecting to untrusted wireless networks", "high"),
            ("Keep client OS and Wi-Fi drivers updated", "medium"),
            ("Educate users on recognising rogue or evil-twin access points", "medium"),
        ],
    },
]

SEVERITY_LABELS = {
    "critical": "CRITICAL",
    "high":     "HIGH    ",
    "medium":   "MEDIUM  ",
    "low":      "LOW     ",
}


def show_hardening_checklist():
    print("\n" + "=" * 60)
    print("      WIRELESS HARDENING CHECKLIST")
    print("=" * 60)
    print("\nUse this checklist to review the security posture of a")
    print("wireless network in an authorized lab or production environment.\n")

    total = 0
    for section in CHECKLIST:
        print(f"\n  [{section['category'].upper()}]")
        for item, severity in section["items"]:
            label = SEVERITY_LABELS.get(severity, "      ")
            print(f"  [ ] [{label}] {item}")
            total += 1

    print("\n" + "-" * 60)
    print(f"  Total items: {total}")
    print("\n  Severity key:")
    print("    CRITICAL — fix immediately, serious risk if unaddressed")
    print("    HIGH     — fix as soon as possible")
    print("    MEDIUM   — fix in normal patch cycle")
    print("    LOW      — fix when convenient")
    print("\n  Tip: Work through each section systematically.")
    print("  Only assess networks you are authorized to review.")
    input("\nPress Enter to return to the main menu...")
