def run_signal_analysis():
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
