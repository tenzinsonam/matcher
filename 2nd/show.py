from pycparser import c_parser, c_ast, parse_file, c_generator




def iterate(node):
	for xname, x in node.children():
		if type(x).__name__ == 'PtrDecl':
			print x.quals
			return x
		else:
			iterate(x)
		






filename = "sample.c"
ast = parse_file(filename)
#node = iterate(ast)
ast.show()
