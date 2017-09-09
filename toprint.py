
from pycparser import c_parser, c_ast, parse_file, c_generator

class BinaryOpVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.values = []
		
	def visit_BinaryOp(self,node):
		self.values.append(node)

class IfVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.values = []
		
	def visit_If(self,node):
		self.values.append(node)

class UnaryOpVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.values = []
		
	def visit_UnaryOp(self,node):
		self.values.append(node)

class AssignmentVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.values = []
		
	def visit_Assignment(self,node):
		self.values.append(node)
		
class DeclVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.values = []
		
	def visit_Decl(self,node):
		self.values.append(node)	
		
def hasChildren(node, p):
	chils = 0
	for yname, y in node.children():
		chils+=1
	if chils is int(p):
		print "same"
	

def rule0(node):
	x0=IfVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=BinaryOpVisitor()
			x2.visit(x1)
			if x2.values:
				for x3 in x2.values:
					for x4 in x3.__slots__:
						if(getattr(x3,x4)=="=="):
							print 'rule0'
def rule1(node):
	x0=AssignmentVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=UnaryOpVisitor()
			x2.visit(x1)
			if x2.values:
				for x3 in x2.values:
					for x4 in x3.__slots__:
						if(getattr(x3,x4)=="p++"):
							print 'rule1'
def rule2(node):
	x0=DeclVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=hasChildren(x1,"2")

ast = parse_file("sample.c")
rule0(ast)
rule1(ast)
rule2(ast)


