def compute(x) :
	y = x.split()
	return " ".join( y[:: -1] )

x = raw_input("please enter the string to reverse :")
print(compute(x))