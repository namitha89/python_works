def dispatch(choice):
	if choice == 'a':
	    function_a()
	elif choice == 'b':
	    function_b()
	elif choice == 'c':
	    function_c()
	else:
	    print "Invalid choice."

def function_a():
	print "function a is selected"

def function_b():
	print "function b is selected"

def function_c():
	print "function c is selected"

dispatch('b')



