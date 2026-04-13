"""
Teaching and help module for the Wireless Toolkit.

Provides short plain-English explanations of the toolkit's core topics,
intended to help beginners understand what each feature does before they
use it.
"""


def explain_topic(topic: str) -> None:
    """Print a plain-English explanation for a given toolkit topic.

    Looks up ``topic`` in a built-in dictionary of explanations and prints
    the result.  If the topic is not recognised, a generic "no explanation
    available" message is printed instead.

    Args:
        topic (str): The topic to explain.  Recognised values are:

            - ``"wifi"``    – Wi-Fi audit feature
            - ``"signal"``  – Signal strength analysis
            - ``"safety"``  – Authorization / safety check
            - ``"report"``  – Report generator
            - ``"notes"``   – Assessment notes helper

    Returns:
        None

    Example::

        >>> explain_topic("wifi")
        [Explain]
        Wireless Check helps review Wi-Fi information such as SSID and encryption type.

        >>> explain_topic("unknown")
        [Explain]
        No explanation available for that topic.
    """
    explanations = {
        "wifi": "Wireless Check helps review Wi-Fi information such as SSID and encryption type.",
        "signal": "Signal Check helps you understand signal strength and whether it looks excellent, good, fair, or weak.",
        "safety": "Safety Check helps confirm that you are working in an approved environment.",
        "report": "Report Generator creates a simple summary of your review and saves it to a file.",
        "notes": "Notes help you document the environment, ownership, approval, and extra observations.",
    }

    print("\n[Explain]")
    print(explanations.get(topic, "No explanation available for that topic."))