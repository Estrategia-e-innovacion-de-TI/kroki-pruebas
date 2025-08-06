import requests

KROKI_URL = "https://kroki.io"

def test_connection_to_api():
    response = requests.get(KROKI_URL)
    assert response.status_code in (200, 404, 405), "API is reachable or responding"

def test_kroki_health_check():
    response = requests.get(f"{KROKI_URL}/health")
    assert response.status_code in (200, 404), "Health endpoint should be reachable if available"
