TERMS = {
    "SSID": (
        "Service Set Identifier. The human-readable name broadcast by a wireless access point "
        "to identify the network."
    ),
    "BSSID": (
        "Basic Service Set Identifier. The MAC address of a wireless access point, uniquely "
        "identifying it on the network."
    ),
    "AP": (
        "Access Point. A networking device that allows wireless clients to connect to a wired "
        "network using Wi-Fi."
    ),
    "WPA2": (
        "Wi-Fi Protected Access 2. A security protocol using AES encryption and CCMP to protect "
        "wireless communications. Widely used and considered strong when properly configured."
    ),
    "WPA3": (
        "Wi-Fi Protected Access 3. The latest Wi-Fi security standard offering stronger encryption "
        "and protection against offline dictionary attacks via SAE (Simultaneous Authentication "
        "of Equals)."
    ),
    "WEP": (
        "Wired Equivalent Privacy. An outdated and insecure wireless encryption protocol from 1999. "
        "Easily cracked; should never be used."
    ),
    "PMF": (
        "Protected Management Frames (IEEE 802.11w). A security extension that encrypts management "
        "frames to protect against spoofing and denial-of-service attacks."
    ),
    "TKIP": (
        "Temporal Key Integrity Protocol. An older encryption method used with WPA. Considered "
        "weak by modern standards and deprecated."
    ),
    "AES": (
        "Advanced Encryption Standard. A strong symmetric encryption algorithm used by WPA2 "
        "and WPA3 to protect wireless traffic."
    ),
    "CCMP": (
        "Counter Mode with CBC-MAC Protocol. The encryption protocol used in WPA2 based on AES. "
        "Provides both confidentiality and data integrity."
    ),
    "SAE": (
        "Simultaneous Authentication of Equals. The handshake protocol introduced in WPA3 that "
        "replaces PSK and provides forward secrecy."
    ),
    "PSK": (
        "Pre-Shared Key. A shared password used in WPA2-Personal mode for authenticating clients "
        "to an access point."
    ),
    "PMKID": (
        "Pairwise Master Key Identifier. A value derived from the PMK, included in the first EAPOL "
        "frame of the WPA2 4-way handshake."
    ),
    "EAPOL": (
        "Extensible Authentication Protocol over LAN. The protocol used to carry EAP messages "
        "over a LAN or wireless network during authentication."
    ),
    "802.11": (
        "A family of IEEE standards for wireless local area networking (WLAN). Common variants "
        "include 802.11a/b/g/n/ac/ax (Wi-Fi 6)."
    ),
    "802.11ax": (
        "Also known as Wi-Fi 6. The latest major Wi-Fi standard offering improved throughput, "
        "efficiency, and multi-user support over 802.11ac."
    ),
    "Channel": (
        "A specific radio frequency range used for wireless communication. The 2.4 GHz band has "
        "14 channels (1-14); the 5 GHz band has many more non-overlapping channels."
    ),
    "DHCP": (
        "Dynamic Host Configuration Protocol. Automatically assigns IP addresses and network "
        "configuration to devices when they connect to a network."
    ),
    "MAC": (
        "Media Access Control address. A unique hardware identifier assigned to a network "
        "interface card (NIC), used at the data-link layer."
    ),
    "IBSS": (
        "Independent Basic Service Set. An ad-hoc wireless network where devices communicate "
        "directly without an access point."
    ),
    "ESS": (
        "Extended Service Set. A group of interconnected access points sharing the same SSID, "
        "enabling roaming across a larger area."
    ),
    "Probe Request": (
        "A frame sent by a wireless client to discover available networks. Can reveal the SSIDs "
        "a device has previously connected to."
    ),
    "Beacon Frame": (
        "A frame periodically broadcast by access points containing the SSID, supported rates, "
        "and capabilities of the network."
    ),
    "Monitor Mode": (
        "A special mode for wireless adapters allowing capture of all wireless frames in range, "
        "regardless of destination. Used passively for analysis."
    ),
    "Promiscuous Mode": (
        "A mode where a network interface captures all packets on a wired segment, not just "
        "those addressed to it. Different from monitor mode (wireless)."
    ),
    "Hidden SSID": (
        "A network configured not to broadcast its SSID in beacon frames. Provides minimal "
        "security benefit as the SSID is revealed in probe requests."
    ),
    "Rogue AP": (
        "An unauthorized access point connected to a network. Can be used by attackers for "
        "man-in-the-middle attacks; detection is a key defensive task."
    ),
    "Deauth": (
        "Deauthentication. A management frame used to terminate a wireless connection. "
        "PMF (802.11w) protects against deauth-based attacks."
    ),
    "Evil Twin": (
        "A rogue access point mimicking a legitimate one to lure clients. Countermeasure: use "
        "certificate-based authentication (802.1X/EAP)."
    ),
    "802.1X": (
        "An IEEE standard for port-based network access control. Used in WPA2/3-Enterprise to "
        "authenticate users via a RADIUS server."
    ),
    "RADIUS": (
        "Remote Authentication Dial-In User Service. A networking protocol providing centralized "
        "authentication for users connecting to a network."
    ),
}


def show_glossary():
    print("\n" + "=" * 60)
    print("        WIRELESS SECURITY GLOSSARY")
    print("=" * 60)
    print("\nAvailable terms:\n")

    terms = sorted(TERMS.keys())
    for i, term in enumerate(terms, 1):
        print(f"  {i:2}. {term}")

    print("\nOptions:")
    print("  Enter a term name to view its definition")
    print("  Enter 'all' to view all definitions")
    print("  Enter 'back' to return to the main menu")

    while True:
        choice = input("\nSearch term (or 'all'/'back'): ").strip()

        if choice.lower() == "back":
            break

        if choice.lower() == "all":
            print()
            for term in sorted(TERMS.keys()):
                print(f"\n  {term}")
                print(f"    {TERMS[term]}")
            break

        match = next(
            (k for k in TERMS if k.lower() == choice.lower()),
            None,
        )
        if match:
            print(f"\n  {match}")
            print(f"    {TERMS[match]}")
        else:
            # Try partial match
            matches = [k for k in TERMS if choice.lower() in k.lower()]
            if matches:
                print("\n  Partial matches found:")
                for m in matches:
                    print(f"\n  {m}")
                    print(f"    {TERMS[m]}")
            else:
                print(f"  Term '{choice}' not found. Try a different spelling.")
