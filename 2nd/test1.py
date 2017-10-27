



def parse(filename):
    fd = open(filename,"r")
    fdw = open("toprint1.py",'w+')
    src = ""
	src += PROLOGUE
    d1 = {}
    d2 = {}
    d3 = {}
    ut = {'hasChildren':'','hasChild':hasChild}
    for line in fd.readlines():
        line0=line.strip()
        line0=line.split('.')
        if()
