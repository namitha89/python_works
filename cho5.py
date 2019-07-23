def compare(a, b):
    """
      >>> compare(5, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 3)
      -1
      >>> compare(42, 1)
      1
    """
    #  Your function body should begin here.
    if(a > b):
      return 1
    elif(a == b):
      return 0
    elif(a < b):
      return -1


compare(5, 4)
compare(7, 7)
compare(2, 3)
compare(42, 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()