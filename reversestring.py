#!/usr/bin/python

def reverse_str(string):
	"""This function reverses the given string in non pythonic way"""
	rstr = ''
	strlen = len(string)
	while strlen > 0:
		rstr += string[strlen-1]
		strlen = strlen-1
	return rstr

print(reverse_str("Can you reverse me"))



# The above solution can be easily solved as given below
string = "This is an example string"
print(string[::-1])

