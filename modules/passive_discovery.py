GUIDANCE = """
PASSIVE WIRELESS DISCOVERY — LEARNING GUIDE
============================================

Passive discovery means observing wireless traffic without transmitting
any frames yourself. Because you are only listening, passive discovery
is the most privacy-respecting and legally cautious form of wireless
reconnaissance — provided you are working in an authorized environment.

---------------------------------------------------------------------
WHAT CAN BE OBSERVED PASSIVELY?
---------------------------------------------------------------------

When an 802.11 adapter is placed in monitor mode it captures:

  • Beacon frames
      - Broadcast periodically by access points (~10/sec by default)
      - Contain: SSID, BSSID (AP MAC), supported data rates, channel,
        encryption capabilities (RSN/WPA IE), country code, PMF flags

  • Probe requests
      - Sent by clients searching for known networks
      - Can reveal SSIDs the device has previously joined
      - Contain client MAC address

  • Probe responses
      - Sent by APs in reply to probe requests
      - Similar content to beacon frames

  • Association / Re-association frames
      - Show which clients are connecting to which APs

  • Data frames (metadata only when encrypted)
      - Reveal active client–AP pairs, traffic volume, timing

---------------------------------------------------------------------
WHAT INFORMATION CAN YOU BUILD?
---------------------------------------------------------------------

From passive capture you can document:

  1. SSIDs and BSSIDs present in the area
  2. Channels in use
  3. Encryption types advertised (WPA2, WPA3, Open)
  4. PMF (Protected Management Frames) support
  5. Vendor of the AP (from OUI of BSSID)
  6. Client device presence and MAC addresses
  7. Signal strength (RSSI) per AP and client

---------------------------------------------------------------------
COMMON PASSIVE TOOLS (for authorized lab use)
---------------------------------------------------------------------

  • Wireshark / tshark
      Capture and inspect 802.11 frames; requires monitor-mode adapter.
      Filter: wlan.fc.type_subtype == 8  (beacon frames)
              wlan.fc.type_subtype == 4  (probe requests)

  • iw / iwlist (Linux)
      Basic scanning using standard OS facilities.
      Command: sudo iw dev <interface> scan

  • nmcli (Linux NetworkManager)
      Non-privileged AP discovery:
      Command: nmcli dev wifi list

  • airport (macOS)
      Built-in scan utility:
      Command: /System/Library/PrivateFrameworks/Apple80211.framework/
               Versions/Current/Resources/airport -s

  • netsh (Windows)
      Command: netsh wlan show networks mode=bssid

---------------------------------------------------------------------
IMPORTANT LEGAL AND ETHICAL NOTES
---------------------------------------------------------------------

  ✔  Passive capture in YOUR OWN lab: generally acceptable.
  ✔  Capture with explicit written authorization: acceptable.
  ✗  Capturing in public spaces or on others' networks without
     authorization: may violate wiretapping / computer fraud laws
     in your jurisdiction.
  ✗  Storing or sharing captured data containing personal information
     without consent: may violate privacy regulations (GDPR, etc.).

  Always obtain written authorization before performing any wireless
  assessment, even passive-only.

---------------------------------------------------------------------
LEARNING EXERCISE IDEAS
---------------------------------------------------------------------

  1. Set up a home lab AP and use nmcli or iw to see what is visible
     before enabling monitor mode.
  2. Enable monitor mode on a test adapter and capture beacons in
     Wireshark. Decode the RSN (Robust Security Network) information
     element to confirm encryption settings.
  3. Compare the SSID list from a passive scan with the list from an
     active scan — note any differences.
  4. Practice documenting your findings in a structured format.
"""


def show_passive_discovery():
    print(GUIDANCE)
    input("Press Enter to return to the main menu...")
