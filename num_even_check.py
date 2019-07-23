def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    count = 0
    for i in str(n):
      if int(i)%2 == 0:
        count = count + 1
    return count  
if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()
    
print(num_even_digits(123456))
print(num_even_digits(2468))
print(num_even_digits(1357))
print(num_even_digits(2))
print(num_even_digits(20))