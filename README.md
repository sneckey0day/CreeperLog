# Red-Team-IP-Leak-Project

## Description
This project demonstrates how to identify and leak the real IP address of a user visiting a website, even if they are using a browser-based VPN. It uses WebRTC for IP leaks and Cloudflare Tunnel for bypassing VPN IPs.

## Features
- **WebRTC Real IP Leak**: Captures the real IP of the user through WebRTC.
- **VPN IP Detection**: Logs the VPN IP address (via Cloudflare headers).
- **Cloudflare Tunnel Integration**: Allows you to easily tunnel a local server to a public URL for testing.

## Setup

### Prerequisites
- Python 3.x
- Cloudflare Tunnel (`cloudflared`)
- Flask (`pip install flask`)

### Running Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/Red-Team-IP-Leak-Project.git
    ```

2. Install dependencies:

    ```bash
    pip install flask
    ```

3. Run the Flask app:

    ```bash
    python logger.py
    ```

4. Tunnel the app with Cloudflare:

    ```bash
    cloudflared tunnel --url http://localhost:8080
    ```

5. Visit the Cloudflare URL (provided by `cloudflared`), and your IP will be logged.

### Log Data
- All logged data will be saved in `logs.txt`.
- Logs contain the real IP, VPN IP, and user details (e.g., browser, timezone).

## Contributions
Feel free to fork and improve the project! Any contributions are welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
