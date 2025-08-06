import pytest
from kroki import diagram_image_bytes, output_formats

@pytest.mark.parametrize("diagram_type,source", [
    ("graphviz", "digraph G {A->B}"),
    ("plantuml", "Alice -> Bob : Hello"),
    ("mermaid", "graph TD; A-->B;")
])
def test_diagram_creation_all_formats(diagram_type, source):
    formats = output_formats.get(diagram_type, [])
    assert formats, f"No formats found for diagram type {diagram_type}"

    for fmt in formats:
        data = diagram_image_bytes(source, diagram_type=diagram_type, output_format=fmt)
        assert isinstance(data, (bytes, bytearray)) and len(data) > 0, f"Failed to generate {fmt} for {diagram_type}"

        if fmt == "png":
            assert data[:8] == b"\x89PNG\r\n\x1a\n"
        elif fmt == "svg":
            assert data.strip().startswith(b"<svg")
