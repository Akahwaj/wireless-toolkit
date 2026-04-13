"""
Platform support check module for the Wireless Toolkit.

Detects the current operating system and checks whether common wireless
analysis tools are available on the system PATH.
"""

import platform
import shutil


def show_platform_support() -> None:
    """Print a platform and tool availability summary to stdout.

    Reports the current operating system and checks whether the following
    command-line tools are installed (i.e. available on ``PATH``):

        - ``nmap``
        - ``tshark``
        - ``tcpdump``
        - ``airodump-ng``

    Returns:
        None

    Example::

        >>> show_platform_support()
        [Platform Support]
        System: Linux
        Python installed: Yes
        Nmap installed: True
        Tshark installed: False
        Tcpdump installed: True
        Airodump-ng installed: False
    """
    print("\n[Platform Support]")
    print(f"System: {platform.system()}")
    print("Python installed: Yes")
    print(f"Nmap installed: {shutil.which('nmap') is not None}")
    print(f"Tshark installed: {shutil.which('tshark') is not None}")
    print(f"Tcpdump installed: {shutil.which('tcpdump') is not None}")
    print(f"Airodump-ng installed: {shutil.which('airodump-ng') is not None}")