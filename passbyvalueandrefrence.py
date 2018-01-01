#!/usr/bin/python

def passbyref(input):
	"""pass by refrence """
	input.append([10,12,13]);
	print "value inside function :",input
	return


a = [100,200,300]
passbyref(a)

print "value outside the function :",a



def passbyvalue(input):
	"""pass by value"""
	input = [10,12,13];
	print "value inside function",input
	return

a = [100,200,500]
passbyvalue(a)

print "value outside the function :",a

