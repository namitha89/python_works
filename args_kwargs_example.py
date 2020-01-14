def displayList(*args,**kwargs):
	print("print the args")
	for i in args:
		print(i)
	print("print the kwargs")
	for j, value in kwargs.items():
		print(j,value)

args = ('Hello', 'Welcome', 'to', 'GeeksforGeeks')
kwargs = {'abc':'hello','efc':'hi','ghk':"rackson"}
displayList(*args, **kwargs)



displayList(7,2,3,4, one="geeks",two="famncy")
