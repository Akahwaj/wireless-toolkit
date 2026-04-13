NOTES = """
PACKET CAPTURE — LEARNING NOTES
=================================

Packet capture (pcap) is the process of recording network traffic for
later analysis. In a wireless context it is one of the most valuable
skills for understanding protocol behavior, verifying security
configurations, and identifying anomalies in an authorized lab.

---------------------------------------------------------------------
CAPTURE FILE FORMATS
---------------------------------------------------------------------

  .pcap (libpcap)
    The original format, supported by virtually every analysis tool.
    Each packet has a simple header: timestamp, length, raw bytes.

  .pcapng (pcap next generation)
    Modern successor. Supports multiple interfaces per file, comments,
    timestamps with nanosecond resolution, and interface descriptions.
    Preferred format for new captures.

---------------------------------------------------------------------
CAPTURE TOOLS
---------------------------------------------------------------------

  Wireshark (GUI)
    Open-source, cross-platform. Best for interactive analysis.
    Website: https://www.wireshark.org

  tshark (CLI — Wireshark's terminal counterpart)
    Syntax:  sudo tshark -i <interface> -w output.pcapng
    Filter:  sudo tshark -i <interface> -f "not arp" -w out.pcapng

  tcpdump (CLI — lightweight, widely available)
    Syntax:  sudo tcpdump -i <interface> -w output.pcap
    Read:    tcpdump -r output.pcap -n

  dumpcap (CLI — capture-only, part of Wireshark)
    Recommended for long-running captures (lower overhead).
    Syntax:  sudo dumpcap -i <interface> -w output.pcapng

---------------------------------------------------------------------
KEY CONCEPTS
---------------------------------------------------------------------

  Capture filter vs. display filter
    Capture filter  — applied at collection time (BPF syntax).
                      Reduces file size; cannot be undone after capture.
                      Example: "wlan type mgt subtype beacon"
    Display filter  — applied in Wireshark after loading the file.
                      Non-destructive. Example: wlan.ssid contains "Lab"

  Ring buffer capture
    Writes to a rotating set of files to limit disk usage.
    tshark: -b filesize:10240 -b files:5   (5 × 10 MB files)

  Timestamps
    Always record captures with accurate system time (use NTP).
    Timestamps are critical when correlating events across devices.

---------------------------------------------------------------------
802.11 FRAME TYPES IN WIRESHARK
---------------------------------------------------------------------

  Management frames (type 0)
    Subtype 0  = Association Request
    Subtype 1  = Association Response
    Subtype 4  = Probe Request
    Subtype 5  = Probe Response
    Subtype 8  = Beacon
    Subtype 11 = Authentication
    Subtype 12 = Deauthentication

  Control frames (type 1)
    Subtype 11 = RTS
    Subtype 12 = CTS
    Subtype 13 = ACK

  Data frames (type 2)
    Encrypted payload in WPA2/3 environments.

  Useful Wireshark filter examples:
    wlan.fc.type_subtype == 8        → beacon frames
    wlan.fc.type_subtype == 4        → probe requests
    eapol                            → WPA handshake frames
    wlan.rsn.akms.type == 2         → WPA2-PSK networks (RSN AKM 2)
    wlan.rsn.akms.type == 8         → SAE (WPA3) networks

---------------------------------------------------------------------
READING A PCAP — CHECKLIST
---------------------------------------------------------------------

  When analysing a wireless capture in Wireshark:

  1. Statistics → Protocol Hierarchy
     Get an overview of frame types present.

  2. Statistics → WLAN Traffic
     Summary of BSS, stations, data rates.

  3. Wireless → WLAN Traffic (in newer Wireshark versions)
     Per-AP and per-client statistics.

  4. Look for:
     • Open (unencrypted) networks in beacon frames
     • Clients probing for networks (probe requests)
     • EAPOL frames (WPA handshake activity)
     • Unusual deauthentication storms (may indicate interference
       or a mis-configured device — not an attack in a clean lab)

---------------------------------------------------------------------
PRIVACY AND LEGAL NOTES
---------------------------------------------------------------------

  ✔  Capture traffic on your own equipment in your own lab.
  ✔  Capture with explicit written authorization from the network owner.
  ✗  Do NOT capture traffic on networks or hardware you do not own or
     have authorization to analyse.
  ✗  Do NOT store or share captures containing personal data without
     appropriate consent and data handling procedures.

  In many jurisdictions, capturing wireless traffic from a network you
  are not authorized to access constitutes a criminal offence.

---------------------------------------------------------------------
LEARNING EXERCISES
---------------------------------------------------------------------

  1. Start a capture with tshark on your monitor-mode interface for
     30 seconds, then open the file in Wireshark.
  2. Apply the display filter:  wlan.fc.type_subtype == 8
     Count how many unique BSSIDs (access points) you see.
  3. Apply the display filter:  wlan.fc.type_subtype == 4
     List the SSIDs requested in probe frames. What do they reveal?
  4. Use Statistics → Protocol Hierarchy to see the split between
     management, control, and data frames.
  5. Export a specific frame as JSON (File → Export Packet Dissections)
     and study the field structure.
"""


def show_packet_capture_notes():
    print(NOTES)
    input("Press Enter to return to the main menu...")
