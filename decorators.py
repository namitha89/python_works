




def login(fun):
	

	def inner(argument):
		print('inside inner')

		if argument == 'naren':
			return fun(argument)
		else:
			return "user not logged in"



	return inner



@login
def homepage(user_name):
	print('inside homepage')
	return "this is home page"


resp = homepage('naren')



print(      resp           )
