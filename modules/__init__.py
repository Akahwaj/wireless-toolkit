"""
Wireless Toolkit – modules package.

Public API
----------
The following functions are importable directly from this package:

.. code-block:: python

    from modules import (
        run_wifi_audit,
        run_signal_analysis,
        authorized_use_check,
        generate_report,
        create_assessment_note,
        explain_topic,
    )
"""

from modules.wifi_audit import run_wifi_audit
from modules.signal_analysis import run_signal_analysis
from modules.safety_checks import authorized_use_check
from modules.report_generator import generate_report
from modules.notes_helper import create_assessment_note
from modules.teach_helper import explain_topic

__all__ = [
    "run_wifi_audit",
    "run_signal_analysis",
    "authorized_use_check",
    "generate_report",
    "create_assessment_note",
    "explain_topic",
]