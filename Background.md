# 📖 WebRTC IP Logging - How It Works

This document explains how the IP logging functionality in this tool works behind the scenes. It's designed to help you understand the technical flow and the Red Teaming value of capturing real IP addresses, even when a user is connected to a VPN.

---

## 🔍 What is WebRTC?
WebRTC (Web Real-Time Communication) is a browser-based technology that enables peer-to-peer communication (like video/audio calls, file sharing, etc.) without any plugins. It uses a mechanism called ICE (Interactive Connectivity Establishment) to figure out how to connect two peers.

---

## ⚙️ Core Component: `RTCPeerConnection`
The JavaScript object `RTCPeerConnection` is used to create a connection between two users. During this process, the browser gathers several IP addresses (called **ICE candidates**) that can be used to establish the connection. These include:

- Local IP addresses (e.g., 192.168.x.x or 10.x.x.x)
- VPN-assigned IP addresses
- Public IPs discovered via STUN servers

---

## 🕳️ How the Leak Happens
Here's the clever part: when we create a peer connection, we can listen for ICE candidates. These contain IP addresses found by the browser, some of which can reveal the user's real public or private IP — even when they are behind a VPN.

### Example Code:
```js
const pc = new RTCPeerConnection({ iceServers: [{ urls: "stun:stun.l.google.com:19302" }] });
pc.createDataChannel("x");
pc.onicecandidate = (e) => {
  if (!e.candidate) return;
  const ip = e.candidate.candidate.match(/([0-9]{1,3}(\.[0-9]{1,3}){3})/);
  if (ip) {
    const realIP = ip[1];
    console.log("[WebRTC Leak] Real IP:", realIP);
  }
};
const offer = await pc.createOffer();
await pc.setLocalDescription(offer);
```

---

## 🔐 Why This Bypasses VPNs
VPNs typically route your internet traffic through an encrypted tunnel. However, WebRTC works differently:

- It directly accesses your network interfaces.
- It can expose internal or public IPs that the VPN doesn’t mask.

That’s why WebRTC leaks are a known privacy issue.

---

## 🎯 Red Team Use Case
For Red Teaming, this technique is useful in phishing pages, recon sites, or C2 panels:

- **Fingerprint targets** more precisely
- **Track real IPs** behind anonymity layers
- **Correlate** internal IPs with corporate environments

---

## 🛡️ Mitigation (For Blue Teams)
- Disable WebRTC in browser settings
- Use browser extensions like WebRTC Leak Prevent
- Use hardened browsers or security-focused OS setups

---

This mechanism is stealthy, browser-based, and doesn’t require any downloads — making it a strong addition to any Red Team recon phase.
