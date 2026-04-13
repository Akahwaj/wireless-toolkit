# 📡 Wireless Security Learning Toolkit

A **defensive, education-focused wireless security toolkit** for lab practice, beginner learning, and authorized wireless assessments.

> ⚠️ **DISCLAIMER — Authorized Use Only**
> This toolkit is intended **solely** for educational purposes, personal lab environments, and explicitly authorized security assessments.
> All features are **passive and informational** — no packet injection, deauthentication, network cracking, rogue AP creation, or any other offensive capability is included or supported.
> **Only use this toolkit on networks and devices you own or have explicit written permission to assess.** Unauthorized access to computer systems and networks is illegal. The authors accept no liability for misuse.

---

## 🚀 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Wireless Glossary** | Definitions for 30+ key wireless security terms (SSID, WPA3, SAE, PMF, and more) with search support |
| 2 | **Wireless Hardening Checklist** | Prioritised checklist (CRITICAL / HIGH / MEDIUM / LOW) covering encryption, authentication, PMF, segmentation, logging, and client security |
| 3 | **Passive Discovery Guidance** | Step-by-step notes on what can be learned by passively observing 802.11 frames, with tool references and legal context |
| 4 | **Monitor Mode Learning Notes** | How monitor mode works, hardware requirements, how to enable it on Linux, and what the Radiotap header contains |
| 5 | **Packet Capture Learning Notes** | pcap/pcapng formats, capture tools (Wireshark, tshark, tcpdump), Wireshark filters, and privacy/legal reminders |
| 6 | **Channel Survey Guidance** | 2.4 / 5 / 6 GHz channel layout, how to conduct a passive channel survey, interpreting RSSI, and tool references |
| 7 | **System Info** | Displays OS, Python version, and checks whether common wireless/capture tools are installed |

---

## 🛠️ Use Cases

- Security learning & practice
- CTF preparation and lab environments
- Wireless assessments (**authorized only**)
- Classroom or self-study reference

---

## ▶️ Quick Start

**Requirements:** Python 3.8 or later. No third-party packages are required for the main toolkit.

```bash
# Clone or download the repository
git clone https://github.com/Akahwaj/wireless-toolkit.git
cd wireless-toolkit

# Run the main toolkit
python3 wireless_toolkit.py
```

You will be greeted with a disclaimer and a numbered menu. Enter the number for the feature you want to explore.

---

## 📂 Project Structure

```
wireless-toolkit/
├── wireless_toolkit.py        # Main entry point — run this
├── modules/
│   ├── glossary.py            # Wireless terminology reference
│   ├── hardening.py           # Wireless hardening checklist
│   ├── passive_discovery.py   # Passive discovery learning guide
│   ├── monitor_mode.py        # Monitor mode learning notes
│   ├── packet_capture.py      # Packet capture learning notes
│   ├── channel_survey.py      # Channel survey guidance
│   ├── system_info.py         # System & tool detection
│   ├── wifi_audit.py          # Wi-Fi configuration audit helper
│   ├── signal_analysis.py     # Signal strength analysis
│   ├── safety_checks.py       # Authorization reminder prompts
│   ├── notes_helper.py        # Assessment notes template generator
│   ├── report_generator.py    # Report generation
│   └── teach_helper.py        # Topic explanation helper
├── core/
│   └── session_store.py       # Session/findings persistence
├── integrations/
│   └── platform_check.py      # Platform and tool availability check
├── app.py                     # Alternative entry point (AEGIS mode)
├── requirements.txt
└── README.md
```

---

## 📖 No Offensive Functionality

This toolkit deliberately excludes:

- ❌ Password or handshake cracking
- ❌ Deauthentication or disassociation attacks
- ❌ Fake / rogue access point creation
- ❌ Packet injection of any kind
- ❌ Any form of unauthorized network access or surveillance

If you are looking for penetration testing tools, please ensure you have the appropriate legal authorization, training, and scope definition before proceeding with any external tooling.

---

## 📜 License

See the [LICENSE](LICENSE) file for details.