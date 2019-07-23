def is_factor(f, n):
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    if n % f == 0:
      return True
    else:
      return False

def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    if is_factor(n, m) == True:
        print True
    else:
        print False






if __name__ == '__main__':
  import doctest
  doctest.testmod()

is_factor(3, 12)
is_factor(5, 12)
is_factor(7, 14)
is_factor(2, 14)
is_factor(7, 15)

is_multiple(12, 3)
is_multiple(12, 4)
is_multiple(12, 5)
is_multiple(12, 6)
is_multiple(12, 7)
