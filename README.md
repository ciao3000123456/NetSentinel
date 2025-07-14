# 🛡️ NetSentinel – Cyber Automation CLI Tool

NetSentinel is a modular and interactive **command-line automation tool** designed for cybersecurity professionals, penetration testers, and ethical hackers. 
It wraps commonly used offensive security tools into a single Python interface for fast deployment, testing, and automation within authorized environments.

---------------

## 🚀 Features

- 🔎 Local network IP sweep (Nmap)
- ⚔️ Launch Metasploit
- 💉 SQLMap guided injection & password extraction
- 🕸️ Burp Suite starter
- 📡 Airgeddon interface launcher
- 🔓 Hashcat password cracking (guided)
- 🔐 Medusa bruteforce (guided)
- 🏭 Modbus Client query assistant (guided)
- ✅ Simple numbered menu with a clean banner

---

## 📦 Requirements

This tool relies on the following system tools:

| Tool         | Install Command                                                    |
|--------------|--------------------------------------------------------------------|
| `nmap`       | `sudo apt install nmap`                                            |
| `msfconsole` | `sudo apt install metasploit-framework`                            |
| `sqlmap`     | `sudo apt install sqlmap`                                          |
| `burpsuite`  | `sudo apt install burpsuite`                                       |
| `airgeddon`  | `git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git`         |
| `hashcat`    | `sudo apt install hashcat`                                         |
| `medusa`     | `sudo apt install medusa`                                          |
| `modbus-cli` | `pip install modbus-cli`                             |

------------

## ⚙️ Usage
------------
### Run the tool


python3 netsentinel.py
-----------------------
Menu Example

===========================================
|         Cyber Automation CLI Tool       |
|             by NetSentinel              |
|       ⚠️ Authorized Use Only ⚠️        |
===========================================

[1] Scan local network (ping sweep)
[2] Launch Metasploit
[3] Launch SQLMap (guided)
[4] Launch Burp Suite
[5] Launch Airgeddon
[6] Launch Hashcat (guided)
[7] Launch Medusa (guided)
[8] Launch Modbus Client (guided)
[9] Exit
-------------------------------------------------------------------
Choose a number to launch the corresponding tool with guided inputs.
-------------------------------------------------------------------
🧪 Examples
Example: SQLMap

Target URL: https://example.com
Cookies (optional): PHPSESSID=xxxxx
Parameters to test: id
Level (1-5): 3
-------------------------------------------------------------------
And a lot of other cool function.
