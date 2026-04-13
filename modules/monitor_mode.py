NOTES = """
MONITOR MODE — LEARNING NOTES
==============================

Monitor mode (also called RFMON — Radio Frequency MONitor mode) allows
a wireless network interface to capture ALL 802.11 frames in range,
not just those addressed to your device. It is the passive equivalent
of promiscuous mode on a wired interface.

---------------------------------------------------------------------
HOW IT DIFFERS FROM MANAGED MODE
---------------------------------------------------------------------

  Managed mode (normal):
    • Associates with a single access point
    • Only passes frames addressed to your MAC (or broadcast/multicast)
    • Driver re-assembles frames; raw 802.11 headers are hidden

  Monitor mode:
    • Does NOT associate with any AP
    • Captures every 802.11 frame the radio can receive on the channel
    • Full 802.11 headers (including management and control frames)
      are visible
    • A Radiotap header is prepended with signal, channel, data rate,
      and antenna metadata

---------------------------------------------------------------------
HARDWARE REQUIREMENTS
---------------------------------------------------------------------

Not all Wi-Fi adapters support monitor mode. Look for:

  • Chipsets with known monitor mode support:
      - Atheros AR9xxx series
      - Ralink/Mediatek RT2xxx, RT3xxx, MT76xx
      - Realtek RTL8812AU / RTL8814AU (with community drivers)
  • USB adapters explicitly marketed for "packet injection" or
    "monitor mode" (useful for lab purchase decisions)
  • Check support: https://aircrack-ng.org/doku.php?id=compatibility_drivers

---------------------------------------------------------------------
ENABLING MONITOR MODE (Linux)
---------------------------------------------------------------------

Method 1 — iw (modern, recommended):

  sudo ip link set <interface> down
  sudo iw dev <interface> set type monitor
  sudo ip link set <interface> up

  Verify: iw dev <interface> info   →  look for "type monitor"

Method 2 — airmon-ng (from aircrack-ng suite):

  sudo airmon-ng start <interface>

  This creates a new interface (commonly <interface>mon or mon0).
  To stop:  sudo airmon-ng stop <interface>mon

Method 3 — iwconfig (legacy, not recommended for new systems):

  sudo iwconfig <interface> mode monitor

---------------------------------------------------------------------
CAPTURING FRAMES IN MONITOR MODE
---------------------------------------------------------------------

  tcpdump (minimal):
    sudo tcpdump -i <monitor_interface> -w capture.pcap

  tshark (more detailed output):
    sudo tshark -i <monitor_interface> -w capture.pcap

  Wireshark (GUI):
    Start Wireshark and select the monitor-mode interface from the list.

  Channel note:
    In monitor mode the adapter listens on one channel at a time.
    Use channel hopping (e.g., with airodump-ng or a custom script)
    to survey multiple channels.

---------------------------------------------------------------------
RADIOTAP HEADER — WHAT IT TELLS YOU
---------------------------------------------------------------------

Every captured packet in monitor mode includes a Radiotap header:

  • Signal strength (RSSI) in dBm       — e.g., -62 dBm
  • Noise level (if available)
  • Channel frequency                    — e.g., 2437 MHz (ch 6)
  • Data rate                            — e.g., 54 Mbit/s
  • RX flags (bad FCS, etc.)

In Wireshark, expand the "Radiotap Header" section to see these fields.

---------------------------------------------------------------------
IMPORTANT NOTES FOR STUDENTS
---------------------------------------------------------------------

  ✔  Monitor mode itself is a passive, listening operation.
  ✔  Use only on networks/hardware you own or have authorization to test.
  ✗  Transmitting (injecting) frames without authorization is illegal
     in most jurisdictions.
  ✗  Capturing traffic on public or third-party networks without
     consent may violate wiretapping laws.

  This toolkit does NOT enable packet injection or any active attack.

---------------------------------------------------------------------
LEARNING EXERCISES
---------------------------------------------------------------------

  1. Enable monitor mode on a spare adapter in your lab. Confirm the
     mode change with `iw dev` and capture a brief beacon-only trace.
  2. Open the capture in Wireshark. Apply the filter:
       wlan.fc.type == 0   (management frames only)
     and explore the beacon and probe frame structures.
  3. Note the Radiotap signal values for different APs. Compare them
     to your estimated distance from each AP.
  4. Document your adapter, chipset, and driver version for your notes.
"""


def show_monitor_mode_notes():
    print(NOTES)
    input("Press Enter to return to the main menu...")
