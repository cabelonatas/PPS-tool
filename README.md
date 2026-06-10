# PPS-tool

PPS-tool is a collection of Python-based security utilities designed for network reconnaissance and web security posture assessment.

## Features

*   **Port Scanner (PPS):** A multithreaded TCP port scanner built with `socket` and `concurrent.futures`, optimized for fast and reliable network auditing.
*   **Security Header Checker (SHC):** A web security tool that analyzes HTTP response headers to evaluate the implementation of modern security standards (e.g., CSP, HSTS, X-Frame-Options).

## Technical Stack

*   **Language:** Python 3.x
*   **Networking:** `socket`, `threading`
*   **Environment:** Cross-platform (developed on Zorin OS)

## Usage

### 1. Requirements
Ensure you have Python installed. Install dependencies if necessary:
```bash
pip install -r requirements.txt

### 2. Running the Tools

*   **Port Scanner:**
```bash
    python3 src/pps.py --target <IP_ADDRESS>
    ```

## Disclaimer
This project is intended for educational purposes and authorized security testing only. The author is not responsible for any misuse of this tool against unauthorized systems.

*   **Security Header Checker:**
```bash
    python3 src/shc.py --url <TARGET_URL>
    ```

## Disclaimer
This project is intended for educational purposes and authorized security testing only. The author is not responsible for any misuse of this tool against unauthorized systems.
