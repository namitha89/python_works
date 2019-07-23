def is_odd(n):
	"""
	>>>is_odd(8)
	True
	>>>is_odd(5)
	False
	>>>is_odd(3)
	False
	>>>is_odd(16)
	True
	"""
	if(n%2 == 0):
		return True
	else:
		return False

if __name__ = '__main__':
	import doctest
	doctest.testmod()

print(is_odd(8))
print(is_odd(5))
print(is_odd(3))
print(is_odd(16))