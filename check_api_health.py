import requests
import time

# Настройки — меняй под свой API
API_URL = "https://api.github.com"  # Пример: GitHub API
TIMEOUT = 10  # секунды на ожидание ответа
MAX_RETRIES = 3  # сколько раз повторить при таймауте

def check_api_health(url=API_URL, timeout=TIMEOUT, retries=MAX_RETRIES):
    for attempt in range(1, retries + 1):
        start_time = time.time()
        try:
            response = requests.get(url, timeout=timeout)
            latency = round(time.time() - start_time, 3)

            # Информация о rate limit (если есть в заголовках)
            rate_remaining = response.headers.get("X-RateLimit-Remaining")
            rate_limit = response.headers.get("X-RateLimit-Limit")

            if response.status_code == 200:
                return {
                    "status": "OK",
                    "latency_sec": latency,
                    "rate_limit_remaining": rate_remaining,
                    "rate_limit_total": rate_limit
                }
            else:
                return {
                    "status": f"ERROR_HTTP_{response.status_code}",
                    "latency_sec": latency,
                    "details": response.text[:200]
                }

        except requests.exceptions.Timeout:
            if attempt < retries:
                print(f"Таймаут, попытка {attempt}/{retries}... Повтор через 2 секунды.")
                time.sleep(2)
                continue
            return {"status": "TIMEOUT", "attempts": retries}

        except requests.exceptions.ConnectionError:
            return {"status": "CONNECTION_ERROR"}
        except Exception as e:
            return {"status": "ERROR", "details": str(e)}

    return {"status": "UNKNOWN_ERROR"}

if __name__ == "__main__":
    print("Проверка здоровья API:", API_URL)
    result = check_api_health()
    print("\nРезультат:")
    for key, value in result.items():
        print(f"  {key}: {value}")
