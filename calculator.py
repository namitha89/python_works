operator = raw_input("Please enter your operator:")
parameter1 = int(raw_input("Please enter parameter one:"))
parameter2 = int(raw_input("please enter parameter two:"))

x = {}
def calculate(opt,x,y):
	
	res = { 

		  '+' : lambda x,y : x + y,
		  '-' : lambda x,y : x - y,
		  '*' : lambda x,y : x * y,
		  '/' : lambda x,y : x / y
		}
	# print(res[opt](x,y))
	return res[opt](x,y)

print(calculate(operator,parameter1,parameter2))

