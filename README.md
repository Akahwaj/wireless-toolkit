# 📡 Wireless Security Toolkit

A **defensive wireless security toolkit** designed for learning, auditing, and lab-based analysis.

---

## ⚡ Quick Start

### Option A – GitHub Codespace (no local install needed)

1. Click **Code → Codespaces → Create codespace on main** on the GitHub repository page.
2. Wait for the container to build (Python 3.12 and all dependencies are installed automatically).
3. In the terminal that opens, run:
   ```bash
   python app.py
   ```

### Option B – Run locally

#### 1. Install Python

| Platform | Instructions |
|----------|-------------|
| **Windows** | Download the installer from [python.org/downloads](https://www.python.org/downloads/). During installation, check **"Add Python to PATH"**. |
| **macOS** | Run `brew install python` (requires [Homebrew](https://brew.sh)), or download from [python.org/downloads](https://www.python.org/downloads/). |
| **Linux (Debian/Ubuntu)** | `sudo apt update && sudo apt install python3 python3-pip` |
| **Android (Termux)** | `pkg install python` |

Verify the installation:
```bash
python --version   # Windows
python3 --version  # macOS / Linux
```
You should see `Python 3.x.x`.

#### 2. Clone the repository

```bash
git clone https://github.com/Akahwaj/wireless-toolkit.git
cd wireless-toolkit
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt      # Windows
pip3 install -r requirements.txt     # macOS / Linux
```

#### 4. Run the toolkit

```bash
python app.py     # Windows
python3 app.py    # macOS / Linux
```

---

## 🚀 Features

- Wi-Fi configuration auditing
- Signal strength analysis
- Safety & authorization checks
- Report generation
- Modular architecture for expansion

---

## 🛠️ Use Cases

- Security learning & practice  
- Lab environments  
- Wireless assessments (authorized only)  
- Documentation & reporting  

---

## 📂 Project Structure