
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
		return 1
	else:
		return 0

def hasChild(node, p):
	for yname, y in node.children():
		if type(y).__name__==p:
			return 1
	return 0

def rule0(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=IfVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=BinaryOpVisitor()
			x2.visit(x1)
			if x2.values:
				for x3 in x2.values:
					for x4 in x3.__slots__:
						if(getattr(x3,x4)=='=='):
							if isFirst:
								nodelist.append(x3)
							else:
								selflist.append(x3)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule0'

def rule1(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=AssignmentVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=UnaryOpVisitor()
			x2.visit(x1)
			if x2.values:
				for x3 in x2.values:
					for x4 in x3.__slots__:
						if(getattr(x3,x4)=='p++'):
							if isFirst:
								nodelist.append(x3)
							else:
								selflist.append(x3)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule1'

def rule2(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=DeclVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=hasChildren(x1,"2")
			if isFirst and x2:
				nodelist.append(x1)
			elif x2:
				selflist.append(x1)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	selflist=[]
	x0=DeclVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=hasChild(x1,"PtrDecl")
			if isFirst and x2:
				nodelist.append(x1)
			elif x2:
				selflist.append(x1)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule2'

def rule3(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=IfVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=hasChild(x1,"Assignment")
			if isFirst and x2:
				nodelist.append(x1)
			elif x2:
				selflist.append(x1)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule3'

def rule4(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=AssignmentVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=UnaryOpVisitor()
			x2.visit(x1)
			if x2.values:
				for x3 in x2.values:
					for x4 in x3.__slots__:
						if(getattr(x3,x4)=="*"):
							if isFirst:
								nodelist.append(x3)
							else:
								selflist.append(x3)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule4'

def rule5(node):
	nodelist = []
	isFirst=1
	selflist=[]
	x0=AssignmentVisitor()
	x0.visit(node)
	if x0.values:
		for x1 in x0.values:
			x2=hasChild(x1,"Assignment")
			if isFirst and x2:
				nodelist.append(x1)
			elif x2:
				selflist.append(x1)
	temp = nodelist[:]
	if not isFirst:
		for m in nodelist:
			if m not in selflist:
				temp.remove(m)
	isFirst=0
	nodelist = temp

	for m in nodelist:
		m.show()
		print 'rule5'


ast = parse_file("sample.c")
rule0(ast)
rule1(ast)
rule2(ast)
rule3(ast)
rule4(ast)
rule5(ast)


