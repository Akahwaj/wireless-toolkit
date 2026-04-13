"""
Wi-Fi audit module for the Wireless Toolkit.

Provides interactive Wi-Fi configuration auditing by prompting the user
for network details (SSID and encryption type) and printing a brief
security review to stdout.
"""


def run_wifi_audit() -> None:
    """Run an interactive Wi-Fi configuration audit.

    Prompts the user to enter the target network's SSID and encryption
    type, then prints an audit summary with a basic security assessment.

    Supported encryption types (case-insensitive):
        - ``open``  – warns that open networks must be used intentionally.
        - ``wpa2``  – notes that WPA3 offers stronger security.
        - ``wpa3``  – confirms strong security.
        - anything else – reported as unknown.

    Returns:
        None

    Example::

        >>> run_wifi_audit()
        [Wi-Fi Audit]
        Enter SSID name: HomeNetwork
        Enter encryption type (WPA2/WPA3/Open): WPA3
        ...
    """
    print("\n[Wi-Fi Audit]")
    ssid = input("Enter SSID name: ").strip()
    encryption = input("Enter encryption type (WPA2/WPA3/Open): ").strip()

    print("\nAudit Summary:")
    print(f"- SSID: {ssid}")
    print(f"- Encryption: {encryption}")

    if encryption.lower() == "open":
        print("- Review: Open networks should only be used intentionally.")
    elif encryption.lower() == "wpa2":
        print("- WPA2 is good, WPA3 is better.")
    elif encryption.lower() == "wpa3":
        print("- Strong security (WPA3).")
    else:
        print("- Unknown encryption.")