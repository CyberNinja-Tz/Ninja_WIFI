# 🥷 Ninja_WIFI v2.0
> **Advanced Wireless Security Auditing Tool (Red Team Edition)**

![Ninja WIFI Banner](https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bHBjNTY2dnlyYnlmaG52ZXJxZmJscmN5YWZ3OHpwZTZocGdvb3lveCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/YPhs6YoPXEJgFxERoG/giphy.gif)

## 📱 Connect with Me
Stay updated with Cyber Security trends and Red Teaming tutorials through my professional channels:

| Platform | Link |
| :--- | :--- |
| **📺 YouTube** | [Nobody Error - Cyber Ninja](https://www.youtube.com/@nobodyerror-q7w2n) |
| **📸 Instagram** | [@cyberninja200](https://www.instagram.com/cyberninja200/) |
| **💼 LinkedIn** | [Cyber Ninja Professional Profile](https://www.linkedin.com/in/cyber-ninja-3a8534399/) |

---

## 📝 Description
**Ninja_WIFI** is a professional Python-based automation tool designed for **Wireless Network Auditing** and **WPA/WPA2 Password Cracking**. It streamlines the workflow for security researchers to perform reconnaissance on local airwaves and test the strength of WiFi credentials using advanced brute-force techniques.

---

## ⚠️ Disclaimer
> [!IMPORTANT]
> This tool is developed for **Educational Purposes and Authorized Penetration Testing only**. The developer (Cyber Ninja) is NOT responsible for any unauthorized use or legal consequences. Cracking networks you do not own or have written permission to test is strictly illegal.

---
🛠️ Requirements

    Kali Linux (or any Debian-based distribution)

    Python 3.x

    pywifi library

    Wireless Adapter (must support managed/monitor mode)



## 🚀 Installation & Usage

To deploy and use **Ninja_WIFI**, follow these steps on your terminal:

### 1. Installation
```bash
# Clone this repository
git clone https://github.com/CyberNinja-Tz/Ninja_WIFI

# Navigate to the directory
cd Ninja_WIFI

# Install required dependencies
pip install pywifi --break-system-packages


---

        ### 2. Usage Guide
# Launch the tool
python Ninja_WIFI.py

# ==========================================
#      STEP-BY-STEP OPERATIONS:
# ==========================================
# 1. scan            : Type 'scan' to list all nearby WiFi networks.
# 2. select          : Choose the index number of your target network.
# 3. change wordlist : Point the tool to your password dictionary (e.g., wordlist.txt).
# 4. attack          : Start the cracking process and wait for the Ninja to find the key.
# 5. help            : Type 'help' anytime to see the full command list.
# ==========================================
