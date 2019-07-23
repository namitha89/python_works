def is_prime(n):
  	"""
      >>> is_prime(5)
      True
      >>> is_prime(3)
      True
    """
 	for i in range(2,n):
 		if ( n % i == 0):
 			return False
 			break
 		else:
 			return True


if __name__ == '__main__':
  import doctest
  doctest.testmod()


print(is_prime(5))

print(is_prime(3))






