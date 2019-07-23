def is_even(n):
	
	"""
      >>> is_even(8)
      True
      >>> is_even(5)
      False
      >>> is_even(3)
      False
      >>> is_even(16)
      True

    """
	if(n%2 == 0):
		return True
	else:
		return False

if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()

print(is_even(8))
print(is_even(5))
print(is_even(3))
print(is_even(16))
