# print round.__doc__
def f2c(t):
    """
      >>> f2c(212)
      100
      >>> f2c(32)
      0
      >>> f2c(-40)
      -40
      >>> f2c(36)
      2
      >>> f2c(37)
      3
      >>> f2c(38)
      3
      >>> f2c(39)
      4
    """
    a = float(t) - 32
    b = float(5)/9
    c = a * b
    return int(round(c))

def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    a = round(t)*float(9)/ 5
    f = round(a) + 32
    return int(f)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
# print(f2c(212))
# print(f2c(32))
# print(f2c(-40))
# print(f2c(36))
# print(f2c(37))
# print(f2c(38))
# print(f2c(39))

print('<<<>>>>')

print(c2f(0))
print(c2f(100))
print(c2f(-40))
print(c2f(12))
print(c2f(18))
print(c2f(-48))

