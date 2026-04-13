#!/usr/bin/env python3
"""
wireless_toolkit.py — Wireless Security Learning Toolkit

A defensive, education-focused toolkit for learning about wireless
security concepts, hardening, and passive analysis techniques.

DISCLAIMER:
  This toolkit is intended SOLELY for educational purposes, personal
  lab environments, and authorized security assessments.  All features
  are passive and informational — no packet injection, deauthentication,
  network cracking, rogue AP creation, or any other offensive capability
  is included or supported.

  Use only on networks and equipment you own or have explicit written
  permission to assess.  Unauthorized access to computer systems and
  networks is illegal.  The authors accept no liability for misuse.
"""

from modules.glossary import show_glossary
from modules.hardening import show_hardening_checklist
from modules.passive_discovery import show_passive_discovery
from modules.monitor_mode import show_monitor_mode_notes
from modules.packet_capture import show_packet_capture_notes
from modules.channel_survey import show_channel_survey
from modules.system_info import show_system_info


DISCLAIMER = """\
============================================================
  WIRELESS SECURITY LEARNING TOOLKIT
  Defensive cybersecurity — education and lab use only
============================================================

  DISCLAIMER: This toolkit is for authorized use only.
  Only use it on networks and devices you own or have
  explicit written permission to assess.
  Unauthorized network access is illegal.
============================================================"""

MENU = """
  MAIN MENU
  ---------
  1. Wireless Glossary
  2. Wireless Hardening Checklist
  3. Passive Discovery Guidance
  4. Monitor Mode Learning Notes
  5. Packet Capture Learning Notes
  6. Channel Survey Guidance
  7. System Info
  0. Exit
"""


def show_main_menu():
    print(DISCLAIMER)
    print(MENU)


def main():
    print(DISCLAIMER)
    while True:
        print(MENU)
        choice = input("  Choose an option: ").strip()

        if choice == "1":
            show_glossary()
        elif choice == "2":
            show_hardening_checklist()
        elif choice == "3":
            show_passive_discovery()
        elif choice == "4":
            show_monitor_mode_notes()
        elif choice == "5":
            show_packet_capture_notes()
        elif choice == "6":
            show_channel_survey()
        elif choice == "7":
            show_system_info()
        elif choice == "0":
            print("\n  Goodbye. Stay safe and authorized.\n")
            break
        else:
            print("\n  Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
