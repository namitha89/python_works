def logical_expression(expression):
	expression = raw_input("Enter boolean expression in two ways :")
	print " p    q       %s" %  expression
	length = len(" p     q    %s" % expression)
	print length*"="

	for p in True, False:
		for q in True, False:
			print "% -7s % -7s % -7s" % (p,q,eval(expression))


logical_expression("p or q")