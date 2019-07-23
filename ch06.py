def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """
    #  Your function body should begin here.
    asq = a**2
    bsq = b**2
    absum = asq + bsq
    c = absum**0.5
    return c



if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()



print(hypotenuse(3, 4))
print(hypotenuse(12, 5))
print(hypotenuse(7, 24))
print(hypotenuse(9, 12))
