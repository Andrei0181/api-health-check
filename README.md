# API Health Check

A lightweight Python utility for checking API availability, measuring response latency, and reporting common request failures.

## Current capabilities

- Sends an HTTP GET request to a configurable API endpoint.
- Reports HTTP status and request latency.
- Handles request timeouts and connection errors.
- Retries timeout failures.
- Displays rate-limit information when the API provides it.

## Requirements

- Python 3.8+
- `requests`

## Quick start

```bash
git clone https://github.com/Andrei0181/api-health-check.git
cd api-health-check
python3 -m pip install requests
python3 check_api_health.py
```

## Configuration

Edit `API_URL` and `TIMEOUT` in `check_api_health.py` to select the endpoint and request timeout.

The current repository contains a basic single-endpoint checker. It is a prototype utility, not a production monitoring platform: it does not currently provide scheduled checks, persistent history, dashboards, or alert delivery.

## Example output

```text
API Health Check Result:
status: OK
latency: 0.245
rate_limit: 4999
```

Actual values depend on the endpoint and response.

## Roadmap

- Support checking multiple endpoints from configuration.
- Add structured JSON output and exit codes for automation.
- Add optional periodic checks and result history.
- Add alert integrations.

## License

No license has been specified yet. All rights remain with the author unless a license is added.
