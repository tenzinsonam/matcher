def print_dict(given):
	fd = open(given,"r")
	fd1 = open("dictfrom","r")
	fd2 = open("2","w")
	
	#line = fd.readline()
	dict1 = ""
	#while(line!="}"):
		#dict1 = dict1 + line
	for line in fd.readlines():
		#print line.strip()
		dict1 = dict1 + line.strip() + "\n"
	dict2 = eval(dict1)
	#print dict1
	#print dict2
	for line1 in fd1.readlines():
		line1 = line1.strip()
		
		list1 = line1.split('.')
		
		list2=[]
		for p in list1:
			if p.find('(')!=-1:
				out = p[0:p.find('(')]
				inn = p[p.find('(')+1:p.find(')')]
				try:
					out = dict2[out]
					inn = dict2[inn]	
				except KeyError:
					out = out
					inn = inn
				tstr = out + '(' + inn + ')'
				list2.append(tstr)
				
			else:
				#print p
				try:
					out = dict2[p]
				except KeyError:
					out = p
				list2.append(out)
		wout = ".".join(list2)
		fd2.write(wout + '\n')
	
	
print_dict("sample1")
