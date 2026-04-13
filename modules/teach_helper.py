def explain_topic(topic: str):
    explanations = {
        "wifi": "Wireless Check helps review Wi-Fi information such as SSID and encryption type.",
        "signal": "Signal Check helps you understand signal strength and whether it looks excellent, good, fair, or weak.",
        "safety": "Safety Check helps confirm that you are working in an approved environment.",
        "report": "Report Generator creates a simple summary of your review and saves it to a file.",
        "notes": "Notes help you document the environment, ownership, approval, and extra observations.",
        "wps": "WPS Audit checks whether Wi-Fi Protected Setup is enabled on a network. WPS PIN mode is vulnerable to brute-force attacks and should be disabled if not needed.",
        "handshake": "Handshake Helper guides you through the WPA/WPA2 handshake capture workflow. A handshake is captured when a client connects to an access point and is used for offline password testing.",
        "mac": "MAC Checker analyzes a MAC address, identifies whether it may be spoofed or locally administered, and explains how to change a MAC address on Linux.",
        "interface": "Interface Helper explains wireless interface modes, provides useful commands for managing interfaces, and checks whether aircrack-ng suite tools are installed.",
    }

    print("\n[Explain]")
    print(explanations.get(topic, "No explanation available for that topic."))
