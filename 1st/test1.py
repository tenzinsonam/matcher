from collections import OrderedDict

# utility functions form prologue
util = ['hasChildren','hasChild']

def givetab(tabcount, funstr):
	i=tabcount
	while i!=0:
		funstr = funstr + "\t"
		i-=1
	return funstr


def norm(ruleno):
	funstr = ""
	tabcount=1
	funstr=givetab(tabcount, funstr)
	funstr+="for m in nodelist:\n"
	tabcount+=1
	funstr=givetab(tabcount, funstr)
	funstr+="m.show()\n"
	funstr=givetab(tabcount, funstr)
	#funstr+="print 'rule"+str(ruleno)+"'\n"
	
	funstr+="print(m.coord.line)\n"
	
	return funstr

def parse(filename):
	fd = open(filename,"r")
	fdw = open("toprint.py",'w+')
	src = ""
	src += PROLOGUE 
	ruleno = 0
	for line in fd.readlines():
		line0 = line.strip()
		list0 = line0.split('&&')
		funstr0 = ""
		funstr0 = givetab(1, funstr0)
		funstr0+="nodelist = []\n"
		funstr0 = givetab(1, funstr0)
		funstr0+="isFirst=1\n"
		for line in list0:
			list1 = line.split('.')
			dict1 = OrderedDict()
			for x in list1:
			#print x
				if x.find('(')==-1:
					dict1[x] = x
				else:
					key = x[0:x.find('(')]
					value = x[x.find('(')+1:x.find(')')]
					dict1[key]=value
				
		#print dict1
		#assert False
			funstr = ""
			tabcount = 1
			funstr = givetab(tabcount, funstr)
			funstr+="selflist=[]\n"
			iter1=0
			for x in dict1:
				if x not in util:
					if x is dict1[x] :
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "x"+str(iter1) + "="+ x + "Visitor("+")\n"  
						funstr = givetab(tabcount, funstr)
						if iter1 == 0:
							funstr = funstr + "x"+str(iter1) + ".visit(node" + ")\n"
						else:
							funstr = funstr + "x"+str(iter1) + ".visit(x" + str(iter1-1) + ")\n"									
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "if x"+str(iter1)+".values:\n"
						tabcount+=1
						iter1+=1
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "for x" + str(iter1) + " in x" + str(iter1-1)+ ".values:\n"
						tabcount+=1
						iter1+=1
				
					else:
					
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "x"+str(iter1) + "="+ x + "Visitor("+")\n"  
						funstr = givetab(tabcount, funstr)
						if iter1 == 0:
							funstr = funstr + "x"+str(iter1) + ".visit(node" + ")\n"
						else:
							funstr = funstr + "x"+str(iter1) + ".visit(x" + str(iter1-1) + ")\n"				
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "if x"+str(iter1)+".values:\n"
						tabcount+=1
						iter1+=1
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "for x" + str(iter1) + " in x" + str(iter1-1)+ ".values:\n"
						tabcount+=1
						iter1+=1
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "for x"+str(iter1)+" in x"+str(iter1-1)+".__slots__:\n"
						tabcount+=1
						funstr = givetab(tabcount, funstr)
						funstr = funstr + "if(getattr(x"+str(iter1-1)+",x"+str(iter1)+")"+"==" + str(dict1[x]) + "):\n"
						iter1+=1
						tabcount+=1
						funstr = givetab(tabcount, funstr)
						funstr += "if isFirst:\n"
						tabcount+=1
						funstr = givetab(tabcount, funstr)				
						funstr += "nodelist.append(x"+str(iter1-2)+")\n"
						#funstr += "print 'rule"+ str(ruleno) + "'"
						tabcount-=1
						funstr = givetab(tabcount, funstr)
						funstr += "else:\n"
						tabcount+=1
						funstr = givetab(tabcount, funstr)
						funstr += "selflist.append(x"+str(iter1-2)+")\n"						
						
				else:
					if x is dict1[x]:
						funstr = givetab(tabcount, funstr)
						funstr += "x"+str(iter1)+"="+str(x) + "(x" + str(iter1-1)+")\n" 
						iter1+=1
						tabcount+=1
					else:
						funstr = givetab(tabcount, funstr)
						funstr += "x"+str(iter1)+"="+str(x) + "(x" + str(iter1-1)+","+str(dict1[x])+")\n" 	
						iter1+=1
						#tabcount+=1
						funstr = givetab(tabcount, funstr)
						funstr += "if isFirst and x"+str(iter1-1)+":\n"
						tabcount+=1
						funstr = givetab(tabcount, funstr)				
						funstr += "nodelist.append(x"+str(iter1-2)+")\n"
						#funstr += "print 'rule"+ str(ruleno) + "'"
						tabcount-=1
						funstr = givetab(tabcount, funstr)
						funstr += "elif x"+str(iter1-1)+":\n"
						tabcount+=1
						funstr = givetab(tabcount, funstr)
						funstr += "selflist.append(x"+str(iter1-2)+")\n"
						
					
					
			tabcount=1
			funstr=givetab(tabcount, funstr)
			funstr+="temp = nodelist[:]\n"
			funstr=givetab(tabcount, funstr)
			funstr+="if not isFirst:\n"
			tabcount+=1
			funstr=givetab(tabcount, funstr)
			funstr+="for m in nodelist:\n"
			tabcount+=1
			funstr=givetab(tabcount, funstr)
			funstr+="if m not in selflist:\n"
			tabcount+=1
			funstr=givetab(tabcount, funstr)
			funstr+="temp.remove(m)\n"
			funstr=givetab(1, funstr)
			funstr+="isFirst=0\n"
			funstr=givetab(1, funstr)
			funstr+="nodelist = temp\n"
			
			
					
			funstr0 +=  funstr + '\n'		
		
		funstr99 = norm(ruleno)
		src += "def rule" + str(ruleno) + "(node):\n" + funstr0 + funstr99 +"\n" 
		ruleno +=1
		#print src
	src += EPILOGUE
	fdw.write(src)
	#print src
				
PROLOGUE = r'''
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

'''			

EPILOGUE = r'''
ast = parse_file("sample.c")
rule0(ast)
rule1(ast)
rule2(ast)
rule3(ast)
rule4(ast)
rule5(ast)


'''



parse("2")
