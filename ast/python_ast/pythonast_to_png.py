#CS620 Demo: Python program AST visualization with a .png file 
#Source: ChatGPT 
#limitations: descriptive labels for graph nodes are provided only for a small subset of Python AST node types.
#Prepared by: Nikhil Hegde

import ast
from graphviz import Digraph
import sys


def ast_to_graph(source_file, output_file="python_ast"):
    # Parse Python source
    with open(source_file, "r") as f:
        source = f.read()

    tree = ast.parse(source, filename=source_file)

    graph = Digraph(
        name="PythonAST",
        format="png"
    )

    graph.attr(
        "node",
        shape="box",
        style="rounded",
        fontname="Helvetica",
        fontsize="10"
    )

    counter = [0]

    def new_id():
        counter[0] += 1
        return f"node{counter[0]}"

    def get_label(node):
        """Create a useful label for each AST node."""

        node_type = type(node).__name__

        # Add useful information to selected nodes
        if isinstance(node, ast.Name):
            return f"Name\\n{node.id}\\nctx={type(node.ctx).__name__}"

        if isinstance(node, ast.Constant):
            return f"Constant\\n{repr(node.value)}"

        if isinstance(node, ast.FunctionDef):
            return f"FunctionDef\\n{node.name}"

        if isinstance(node, ast.arg):
            return f"arg\\n{node.arg}"

        if isinstance(node, ast.Attribute):
            return f"Attribute\\n{node.attr}"

        if isinstance(node, ast.alias):
            return f"alias\\n{node.name} as {node.asname}"

        if isinstance(node, ast.keyword):
            return f"keyword\\n{node.arg}"

        if isinstance(node, ast.operator):
            return node_type

        if isinstance(node, ast.unaryop):
            return node_type

        if isinstance(node, ast.boolop):
            return node_type

        return node_type

    def visit(node, parent_id=None, field_name=None):
        node_id = new_id()

        label = get_label(node)

        # Include field name in edge label when available
        graph.node(node_id, label)

        if parent_id is not None:
            if field_name:
                graph.edge(parent_id, node_id, label=field_name)
            else:
                graph.edge(parent_id, node_id)

        # IMPORTANT:
        # iter_fields() gives us both the field name and child node.
        for field, value in ast.iter_fields(node):

            if isinstance(value, ast.AST):
                visit(value, node_id, field)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        visit(item, node_id, field)

        return node_id

    visit(tree)

    graph.render(output_file, cleanup=True)

    print(f"Generated: {output_file}.png")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} program.py")
        sys.exit(1)

    ast_to_graph(sys.argv[1])
