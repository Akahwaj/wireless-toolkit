GUIDANCE = """
CHANNEL SURVEY — LEARNING GUIDE
=================================

A channel survey (also called a wireless site survey) documents which
channels are in use, how congested they are, and how access points
overlap — all without transmitting any data yourself.

Understanding the RF environment helps you:
  • Identify interference sources
  • Optimise channel assignment for new deployments
  • Detect rogue or unexpected access points
  • Validate that your own APs are configured correctly

---------------------------------------------------------------------
802.11 CHANNEL BASICS
---------------------------------------------------------------------

  2.4 GHz band
  ─────────────
    Channels 1–14 (varies by country; 1–11 in USA, 1–13 in most of EU)
    Channel width: 20 MHz (standard), 40 MHz (HT40, overlapping)
    Non-overlapping channels: 1, 6, 11  (in 20 MHz mode)

    Overlap example:
      Channel 1 occupies ≈ 2401–2423 MHz
      Channel 6 occupies ≈ 2426–2448 MHz
      Channel 11 occupies ≈ 2451–2473 MHz
      → Channels 2–5 and 7–10 overlap with neighbours, causing
        co-channel and adjacent-channel interference.

  5 GHz band
  ───────────
    Many more non-overlapping channels (36, 40, 44, 48 — UNII-1, etc.)
    Higher throughput, shorter range, less congested.
    DFS (Dynamic Frequency Selection) channels avoid radar systems.

  6 GHz band (Wi-Fi 6E / 802.11ax)
  ──────────────────────────────────
    New spectrum; channels 1–233 (subject to country regulations)
    Completely separate from 2.4/5 GHz interference.

---------------------------------------------------------------------
HOW TO CONDUCT A CHANNEL SURVEY (PASSIVE / OBSERVATIONAL)
---------------------------------------------------------------------

  Step 1 — Document your environment
    Note the floor plan or area dimensions, wall materials, and the
    expected number of APs to survey.

  Step 2 — Select the appropriate band(s)
    Start with 2.4 GHz (most crowded), then 5 GHz, then 6 GHz if
    Wi-Fi 6E is present.

  Step 3 — Scan with available OS tools
    Linux:
      sudo iw dev <interface> scan | grep -E "BSS|freq|SSID|signal"

    Windows:
      netsh wlan show networks mode=bssid

    macOS:
      /System/Library/PrivateFrameworks/Apple80211.framework/
      Versions/Current/Resources/airport -s

  Step 4 — Note for each AP:
    • BSSID (MAC address)
    • SSID
    • Channel / frequency
    • Signal strength (RSSI in dBm)
    • Security type (WPA2, WPA3, Open)

  Step 5 — Map channel utilisation
    Create a simple table or tally:

      Channel | Count of APs | Notes
      --------+--------------+----------------------------
        1     |    3         | Your AP, neighbour AP x2
        6     |    1         | Guest AP
        11    |    2         | Office AP, visitor AP
        36    |    1         | 5 GHz corporate AP

  Step 6 — Identify congestion
    If more than 2–3 APs share the same non-overlapping channel at
    overlapping signal levels, co-channel interference likely degrades
    performance.

  Step 7 — Document and report findings
    Record your observations for review or handoff to network staff.

---------------------------------------------------------------------
INTERPRETING SIGNAL STRENGTH (RSSI)
---------------------------------------------------------------------

  dBm value  | Quality         | Expected use
  -----------+-----------------+-----------------------------
  > -50 dBm  | Excellent       | Very close to AP
  -50 to -67 | Good            | Normal working distance
  -67 to -75 | Fair            | Acceptable for most tasks
  -75 to -85 | Weak            | Packet loss likely
  < -85 dBm  | Very weak       | Unreliable connection

  Note: dBm is a logarithmic scale.
    -60 dBm is ~10× stronger than -70 dBm (10 dB = 10× power ratio).

---------------------------------------------------------------------
CHANNEL SURVEY TOOLS (EDUCATIONAL REFERENCE)
---------------------------------------------------------------------

  • Wireshark (with monitor mode)
      Display filter:  wlan.fc.type_subtype == 8  (beacons)
      Use Statistics → WLAN Traffic for a summary.

  • iw scan (Linux, no monitor mode needed for basic scan)
      Provides frequency, SSID, BSSID, signal for visible APs.

  • inSSIDer (Windows/macOS, free version available)
      GUI channel graph — helpful for visualising overlap.

  • Kismet (Linux, open source)
      Passive WLAN discovery with channel hopping; stores logs to file.
      Run in monitor mode for full capture.

---------------------------------------------------------------------
NOTES ON CHANNEL HOPPING
---------------------------------------------------------------------

  A wireless adapter can only listen on ONE channel at a time.
  "Channel hopping" means rapidly switching between channels to survey
  multiple channels over time.

  Tools like Kismet or custom scripts cycle through channels
  (e.g., 1→6→11→36→40→44…) spending a dwell time (typically 100–200 ms)
  on each. This means you may miss short-lived frames on any given
  channel — accept this as a trade-off for breadth of coverage.

---------------------------------------------------------------------
LEGAL AND ETHICAL REMINDERS
---------------------------------------------------------------------

  ✔  Surveying your own network and lab environment: acceptable.
  ✔  Surveying with written authorization: acceptable.
  ✗  Actively probing or scanning neighbour networks: not authorized.
  ✗  Recording client traffic or personal data: requires consent and
     legal basis.

---------------------------------------------------------------------
LEARNING EXERCISES
---------------------------------------------------------------------

  1. Use nmcli or iw to list all APs visible from your location.
     Tally which channels are used and identify any congestion.
  2. Draw a simple 2.4 GHz channel map on paper. Mark overlapping
     channels and suggest a better assignment if needed.
  3. Compare signal strengths from the same AP in two different rooms.
     Calculate the approximate dB loss through the wall.
  4. If you have a spare monitor-mode adapter, use Kismet for 5 minutes
     to capture beacons. Review the channel distribution in the logs.
"""


def show_channel_survey():
    print(GUIDANCE)
    input("Press Enter to return to the main menu...")
