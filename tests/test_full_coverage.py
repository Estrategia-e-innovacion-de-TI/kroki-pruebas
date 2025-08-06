import pytest
from kroki import diagram_types, diagram_image_bytes, output_formats

@pytest.mark.parametrize("diagram_type", diagram_types)
def test_all_supported_types(diagram_type):
    formats = output_formats.get(diagram_type, [])
    assert formats, f"No formats found for {diagram_type}"

    # Simplified default diagram source examples
    default_sources = {
        "graphviz": "digraph G {A->B}",
        "plantuml": "@startuml\nAlice -> Bob\n@enduml",
        "mermaid": "graph TD; A-->B;"
    }
    source = default_sources.get(diagram_type, "test")

    for fmt in formats:
        try:
            data = diagram_image_bytes(source, diagram_type=diagram_type, output_format=fmt)
            assert data and isinstance(data, (bytes, bytearray)), f"{diagram_type}/{fmt} failed"
        except Exception as e:
            pytest.fail(f"{diagram_type}/{fmt} raised error: {e}")
