# api-health-check
Simple Python script for API health checks, latency measurement and error handling
Updated README# API Health Check

A Python script to check the health of APIs by measuring their response time (latency), handling errors, and reporting the status. 

## Features
- Checks API health with status code and latency
- Handles different types of errors like timeouts, connection issues, etc.
- Supports retry logic for timeouts
- Shows rate limit information (if available)

## Requirements
- Python 3.6+
- `requests` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/berestov0181/api-health-check.git
pip install requests
python3 check_api_health.py


---

### 2. **Заливка кода в репозиторий**

1. Создаём файл с кодом. В репозитории на GitHub, в каталоге репозитория создаем новый файл:

```plaintext
check_api_health.py
import requests
import time

API_URL = "https://api.github.com"
TIMEOUT = 10


def check_api_health():
    start = time.time()
    try:
        response = requests.get(API_URL, timeout=TIMEOUT)
        latency = time.time() - start

        if response.status_code == 200:
            return {
                "status": "OK",
                "latency": round(latency, 3),
                "rate_limit": response.headers.get("X-RateLimit-Remaining")
            }
        else:
            return {
                "status": f"HTTP_{response.status_code}",
                "latency": round(latency, 3)
            }

    except requests.exceptions.Timeout:
        return {"status": "TIMEOUT"}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}


if __name__ == "__main__":
    result = check_api_health()
    print("API Health Check Result:")
    for k, v in result.items():
        print(f"{k}: {v}")

