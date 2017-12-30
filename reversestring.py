#!/usr/bin/python

def reversestr(str):
	rstr = ''
	strlen = len(str)
	while strlen > 0:
		rstr += str[strlen-1]
		strlen = strlen-1
	return rstr

print(reversestr("namitha hi narendra hi hi"))



## the above solution can be easily solved as given below




str = "namitha hi narendra hi hi"
print(str[::-1])

