import pytest

@pytest.fixture(scope="session")
def kroki_url():
    return "https://kroki.io"

@pytest.fixture(scope="session")
def example_sources():
    return {
        "graphviz": "digraph G {A->B}",
        "plantuml": "@startuml\nAlice -> Bob\n@enduml",
        "mermaid": "graph TD; A-->B;"
    }
