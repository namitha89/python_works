#!/usr/bin/python

def swap_string(a, b):
	a, b = b, a
	return a, b;

output1, output2 = swap_string(10, 5)

print "output1 = {} and output2 = {}".format(output1, output2)
