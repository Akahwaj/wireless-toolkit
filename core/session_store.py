import json
from pathlib import Path


SESSION_FILE = Path("output/session_data.json")


def load_session():
    if not SESSION_FILE.exists():
        return {"findings": []}
    try:
        return json.loads(SESSION_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"findings": []}


def save_session(data):
    SESSION_FILE.parent.mkdir(exist_ok=True)
    SESSION_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def add_finding(title, severity, details, recommendation):
    data = load_session()
    data.setdefault("findings", []).append({
        "title": title,
        "severity": severity,
        "details": details,
        "recommendation": recommendation,
    })
    save_session(data)