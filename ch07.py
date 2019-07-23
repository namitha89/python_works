def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    y = float(y2 - y1)
    x = float(x2 - x1)
    yx = float(y/x)
    return yx

def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0

    """
    y = y2 - (slope(x1,y1,x2,y2) * x2)
    return y 



if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()

print(slope(5, 3, 4, 2))
print(slope(5, 3, 4, 2))
print(slope(2, 4, 1, 2))
print(intercept(1, 6, 3, 12))
print(intercept(6, 1, 1, 6))
print(intercept(4, 6, 12, 8))