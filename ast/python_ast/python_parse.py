#CS620 Demo: Python program to dump the ast of matmul_cmplx.py on the terminal.
#Author: Nikhil Hegde
import ast

with open("matmul_cmplx.py", "r") as f:
    source = f.read()

tree = ast.parse(source)

#exercise: how do you dump the line numbers along with AST nodes?
print(ast.dump(tree, indent=4, include_attributes=True))


