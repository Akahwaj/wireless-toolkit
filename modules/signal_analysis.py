"""
Signal analysis module for the Wireless Toolkit.

Provides interactive Wi-Fi signal strength analysis, mapping raw dBm
values to human-readable quality ratings.
"""


def run_signal_analysis() -> None:
    """Run an interactive Wi-Fi signal strength analysis.

    Prompts the user for a signal strength value in dBm, then prints a
    signal quality rating based on the following thresholds:

    +-----------------+--------------------+
    | dBm range       | Quality rating     |
    +=================+====================+
    | >= -50 dBm      | Excellent signal   |
    +-----------------+--------------------+
    | -67 to -51 dBm  | Good signal        |
    +-----------------+--------------------+
    | -75 to -68 dBm  | Fair signal        |
    +-----------------+--------------------+
    | < -75 dBm       | Weak signal        |
    +-----------------+--------------------+

    Returns:
        None

    Raises:
        Prints an error message and returns early if the input cannot be
        parsed as an integer; no exception is propagated to the caller.

    Example::

        >>> run_signal_analysis()
        [Signal Analysis]
        Enter signal strength in dBm (example: -67): -60
        Signal Review:
        - Signal Strength: -60 dBm
        - Good signal
    """
    print("\n[Signal Analysis]")
    try:
        signal_strength = int(input("Enter signal strength in dBm (example: -67): ").strip())
    except ValueError:
        print("Invalid signal strength.")
        return

    print("\nSignal Review:")
    print(f"- Signal Strength: {signal_strength} dBm")

    if signal_strength >= -50:
        print("- Excellent signal")
    elif signal_strength >= -67:
        print("- Good signal")
    elif signal_strength >= -75:
        print("- Fair signal")
    else:
        print("- Weak signal")
