def string_operation(string):
  """
  >>> type(fruit)
  <type 'str'>
  >>> len(fruit)
  8
  >>> fruit[:3]
  'ram'
"""
  fruit = str(string);
  print(type(fruit))
  print(len(fruit))
  print(fruit[:3])

if __name__ == '__main__':
	import doctest
	doctest.testmod()

string_operation('ramphala')