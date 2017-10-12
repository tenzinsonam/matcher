from pycparser import c_parser, c_ast, parse_file, c_generator
import copy

ut = ['hasChildren','hasChild']     #utiltity functions
d1 = {'Assignment':'','If':''}    #info classes as per types
d2 = {'1':{'UnaryOp':'p++'},'2':{'BinaryOp':'=='},'3':{'hasChild':'Assignment'}}    #rule attributes #for checking if it contains sometype put the value for this 'sometype' key as -1
d3 = {'Assignment':['1'],'If':['2','3']}   
st1 = []                    #stack used in dfs

###############
#space=0


#############

class info:     #basic info class
    def __init__(self):
        self.rule=[]
        self.fields={}    


def func1():    #implementing info for all d1 elements
    
    for w in d1:
        t99 = info()
        #print(t99.rule)
        for x in d3[w]:
            t99.rule.append(x)
            for y in d2[x]:
                t99.fields[y]=-1
        d1[w]=copy.deepcopy(t99)
        #print(d1[w].fields)
    #assert False
        


def check_rule(temp):   #checks if any rule is satisfied by node
    #print(temp.fields)
    #assert False
    for x in temp.rule:
        chk=0           #checks at particular rule
        for y in d2[x]:
            chk1=0
            if(d2[x][y] is not -1):     #obsolete
                try:
                    for z in temp.fields[y][1]:
                        #print temp.fields[y][0]
                        #print(getattr(temp.fields[y][0],z))
                        #print(d2[x][y] + '\n')
                        if(d2[x][y] == getattr(temp.fields[y][0],z)):
                            #print(d1['Assignment'].fields)
                            chk1=1
                except TypeError:
                    continue
            else:
                if(y in temp.fields):
                    
                    chk1=1
            if(chk1 == 0):
                break
        if(chk1):
            return True
    return False
    




def dfs(node, inf):
    #print(type(node).__name__ + '\n')        
    if(inf is not None):
        if(type(node).__name__ in inf.fields):
            fd=0
            #print(d1['Assignment'].fields)
            inf.fields[type(node).__name__] = [node,node.__slots__] #node and node__slots__
            #print(d1['Assignment'].fields)
            #print(getattr(inf.fields['UnaryOp'][0],'op'))
            #print([node,node.__slots__])
            ##assert False
            
    if(type(node).__name__ in d1):
        t1 = copy.deepcopy(d1[str(type(node).__name__)])
        #print(d1[str(type(node).__name__)].fields)
        #st1.append(t1)
        for xname, x in node.children():
            dfs(x,t1)

       
        #t1 = st1.pop()
        #print(t1.fields)
        #assert False
        if(check_rule(t1)):
            #assert False
            print(str(node)+' '+type(node).__name__ + '\n')
            #print(d1[str(type(node).__name__)])
            #assert False
            print("works")
        
    else:
        for xname, x in node.children():
            dfs(x,inf)
        


func1()     #populate Assignmwnt info class 
#assert False
ast=parse_file("sample.c")
dfs(ast,None)

#print(d1['Assignment'].fields)


