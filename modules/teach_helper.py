def explain_topic(topic: str):
    explanations = {
        "wifi": "Wireless Check helps review Wi-Fi information such as SSID and encryption type.",
        "signal": "Signal Check helps you understand signal strength and whether it looks excellent, good, fair, or weak.",
        "safety": "Safety Check helps confirm that you are working in an approved environment.",
        "report": "Report Generator creates a simple summary of your review and saves it to a file.",
        "notes": "Notes help you document the environment, ownership, approval, and extra observations.",
    }

    print("\n[Explain]")
    print(explanations.get(topic, "No explanation available for that topic."))