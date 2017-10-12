from pycparser import c_parser, c_ast, parse_file, c_generator


ast = parse_file("sample.c")
ast.show()

#visit(ast)
