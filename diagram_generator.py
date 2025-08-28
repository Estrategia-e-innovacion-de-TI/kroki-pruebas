"""
Kroki Diagram Generator Script

This script takes a text file containing diagram source code and generates
an SVG image using the Kroki library.

Usage:
    python kroki_generator.py <input_file.txt> <diagram_type> [output_file.svg]

Example:
    python kroki_generator.py graph.txt graphviz diagram.svg
    python kroki_generator.py uml.txt plantuml
    python kroki_generator.py flow.txt mermaid flowchart.svg
"""

import argparse
import sys
from pathlib import Path
from kroki import diagram_image_bytes, output_formats


def validate_diagram_type(diagram_type):
    """Validate if the diagram type is supported by Kroki."""
    available_formats = output_formats.get(diagram_type)
    if not available_formats:
        raise ValueError(f"Unsupported diagram type: {diagram_type}")
    
    if "svg" not in available_formats:
        raise ValueError(f"SVG output not supported for diagram type: {diagram_type}")
    
    return True


def read_diagram_source(file_path):
    """Read the diagram source code from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
        
        if not content:
            raise ValueError(f"Input file {file_path} is empty")
        
        return content
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")
    except UnicodeDecodeError:
        raise ValueError(f"Cannot read file {file_path}. Please ensure it's a valid text file.")


def generate_diagram(source_code, diagram_type):
    """Generate diagram image bytes using Kroki."""
    try:
        image_data = diagram_image_bytes(
            source_code, 
            diagram_type=diagram_type, 
            output_format="svg"
        )
        
        if not image_data or len(image_data) == 0:
            raise RuntimeError("Generated image data is empty")
        
        # Validate SVG format
        if not image_data.strip().startswith(b"<svg"):
            raise RuntimeError("Generated data is not a valid SVG image")
        
        return image_data
    
    except Exception as e:
        raise RuntimeError(f"Failed to generate diagram: {str(e)}")


def save_image(image_data, output_path):
    """Save the image data to an SVG file."""
    try:
        with open(output_path, 'wb') as file:
            file.write(image_data)
        print(f"Diagram successfully saved to: {output_path}")
    
    except Exception as e:
        raise RuntimeError(f"Failed to save image to {output_path}: {str(e)}")


def get_default_output_filename(input_file, diagram_type):
    """Generate a default output filename based on input file and diagram type."""
    input_path = Path(input_file)
    base_name = input_path.stem
    return f"{base_name}_{diagram_type}.svg"


def main():
    parser = argparse.ArgumentParser(
        description="Generate SVG diagrams from text files using Kroki",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported diagram types include:
- graphviz: For directed/undirected graphs
- plantuml: For UML diagrams
- mermaid: For flowcharts, sequence diagrams, etc.
- blockdiag: For block diagrams
- bpmn: For business process diagrams
- bytefield: For network packet diagrams
- seqdiag: For sequence diagrams
- actdiag: For activity diagrams
- nwdiag: For network diagrams
- packetdiag: For packet diagrams
- rackdiag: For rack diagrams
- c4plantuml: For C4 model diagrams
- ditaa: For ASCII art diagrams
- erd: For entity relationship diagrams
- excalidraw: For hand-drawn style diagrams
- nomnoml: For UML diagrams
- pikchr: For diagrams
- structurizr: For software architecture diagrams
- svgbob: For ASCII to SVG diagrams
- vega: For data visualizations
- vegalite: For data visualizations
- wavedrom: For digital timing diagrams

Example usage:
    python kroki_generator.py graph.txt graphviz
    python kroki_generator.py sequence.txt plantuml my_diagram.svg
        """
    )
    
    parser.add_argument(
        'input_file', 
        help='Path to the text file containing diagram source code'
    )
    
    parser.add_argument(
        'diagram_type', 
        help='Type of diagram (e.g., graphviz, plantuml, mermaid)'
    )
    
    parser.add_argument(
        'output_file', 
        nargs='?', 
        help='Output SVG file path (optional, auto-generated if not provided)'
    )
    
    parser.add_argument(
        '--list-formats',
        action='store_true',
        help='List all supported diagram types and their available formats'
    )

    args = parser.parse_args()

    # Handle list formats option
    if args.list_formats:
        print("Supported diagram types and their output formats:")
        print("-" * 50)
        for diagram_type, formats in sorted(output_formats.items()):
            svg_supported = "✓" if "svg" in formats else "✗"
            print(f"{diagram_type:15} | SVG: {svg_supported} | Formats: {', '.join(formats)}")
        return 0

    try:
        validate_diagram_type(args.diagram_type)
        
        print(f"Reading diagram source from: {args.input_file}")
        source_code = read_diagram_source(args.input_file)
        
        if args.output_file:
            output_file = args.output_file
        else:
            output_file = get_default_output_filename(args.input_file, args.diagram_type)
        
        if not output_file.lower().endswith('.svg'):
            output_file += '.svg'
        
        print(f"Generating {args.diagram_type} diagram...")
        image_data = generate_diagram(source_code, args.diagram_type)
        
        save_image(image_data, output_file)
        
        return 0

    except (ValueError, FileNotFoundError, RuntimeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 1
    
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())