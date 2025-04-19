## ⚡ IP Recon Logger — Stealth IP Capture Tool

A stealth browser-based recon tool that silently captures real IP addresses, even when a VPN is in use, using WebRTC leaks and fallback techniques. It also logs User-Agent, timezone, language, and more — while showing a decoy page to the target. Perfect for Red Team recon and footprinting.

## 📸 Screenshot

![Screenshot](assets/screenshot.png)

---

### 🔥 Features
- Captures **WebRTC**
- Logs **User-Agent**, **Language**, and **Timezone**
- Backend logs are **hidden from the user**
- Clean **terminal output in table format**
- Supports **Cloudflared** tunneling for WAN access
- Saves everything in `logs.txt`

---

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/sneckey0day/CreeperLog
cd CreeperLog

# Install requirements
pip install flask
pip install prettytable
```

---

### 🚀 Running the Tool

```bash
# Start the Flask server
python3 logger.py
```

The server will be available on:
```
http://localhost:8080
```

---

### 🌐 Make It Public with Cloudflared

Cloudflared creates a public tunnel to localhost — perfect for Red Team stealth drops.

#### 📥 Install Cloudflared:

```bash
# Debian/Ubuntu
sudo apt install cloudflared

# OR download manually
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
```

#### 🚇 Run Cloudflared Tunnel

```bash
cloudflared tunnel --url http://localhost:8080
```

#### ⚙️ Optional Flags

| Flag                      | Description                                 |
|---------------------------|---------------------------------------------|
| `--url`                   | Local server to expose                      |
| `--no-autoupdate`         | Prevent Cloudflared from auto-updating     |
| `--loglevel info/warn`    | Control verbosity of tunnel output         |
| `--metrics 0.0.0.0:XXX`   | Expose metrics endpoint                     |

Example with extras:

```bash
cloudflared tunnel --url http://localhost:8080 --no-autoupdate --loglevel info
```

---

### 📁 File Structure

```
.
├── index.html      # Frontend IP collection (stealth mode)
├── logger.py       # Backend Flask server (logs and prints)
├── logs.txt        # Output logs
├── README.md       # This doc
```

---

### 📋 Sample Terminal Log Output

```
========================================
               LOGGED DATA               
========================================
Source              | IP              | User-Agent                    | Timezone        
----------------------------------------
WebRTC              | 192.168.1.2     | Mozilla/5.0 (Windows NT 10.0) | Asia/Kolkata
========================================
```

---

### ⚠️ Disclaimer

This tool is intended **strictly for educational and authorized testing purposes**. Use responsibly in environments you have **explicit permission** to test.
