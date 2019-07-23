def print_digits(n):
    """
      >>> print_digits(13789)
      9 8 7 3 1
      >>> print_digits(39874613)
      3 1 6 4 7 8 9 3
      >>> print_digits(213141)
      1 4 1 3 1 2
    """
    
    digits = '';
    rev = str(n)
    rev1 = rev[:: -1]
    for i in rev1:
    	digits = digits +' '+ i
    print(digits)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

print_digits(13789)
print_digits(39874613)
print_digits(213141)
