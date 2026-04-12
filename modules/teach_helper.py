def explain_topic(topic: str):
    explanations = {
        "wifi": "Wireless Check helps review Wi-Fi information such as SSID and encryption type.",
        "signal": "Signal Check helps you understand signal strength and quality.",
        "safety": "Safety Check confirms you are working in an approved environment.",
        "report": "Report Generator creates a simple summary of your review.",
        "notes": "Notes help document your environment, approval, and observations.",
    }

    print("\n[Explain]")
    print(explanations.get(topic, "No explanation available."))
