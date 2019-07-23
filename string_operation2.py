def string_operation():
  """
  >>> group = "John, Paul, George, and Ringo"
  >>> group[12:x]
  'George'
  >>> group[n:m]
  'Paul'
  >>> group[:r]
  'John'
  >>> group[s:]
  'Ringo'
"""
if __name__ == '__main__':
	import doctest
	doctest.testmod()

group = "John, Paul, George, and Ringo"

print(group[12:18])
print(group[6:10])
print(group[:4])
print(group[23:29])
