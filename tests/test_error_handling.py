import requests

KROKI_URL = "https://kroki.io"

def test_invalid_diagram_source():
    payload = {
        "diagram_source": "@startuml\ninvalid-diagram\n@enduml",
        "diagram_type": "plantuml",
        "output_format": "svg"
    }
    response = requests.post(f"{KROKI_URL}/", json=payload)
    assert response.status_code in (400, 422)

def test_unsupported_format():
    payload = {
        "diagram_source": "graph TD; A-->B;",
        "diagram_type": "mermaid",
        "output_format": "bmp"  # unsupported
    }
    response = requests.post(f"{KROKI_URL}/", json=payload)
    assert response.status_code in (400, 415)

def test_missing_fields():
    payload = {"diagram_type": "graphviz"}  # missing diagram_source and output_format
    response = requests.post(f"{KROKI_URL}/", json=payload)
    assert response.status_code in (400, 422)
