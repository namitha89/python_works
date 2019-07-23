#Open a file named ch09e02.py and with the following content:
#Add each of the following sets of doctests to the docstring at the top of the file and write Python code to make the doctests pass.
def list_operation():
#  Add your doctests here:
  """
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""
  b_list = ['hkjjk','Stills', 'Nash']
  c_list = ['Young']

  print(b_list[1:])
  group = b_list + c_list
  print(group[-1])




# Write your Python code here:


if __name__ == '__main__':
    import doctest
    doctest.testmod()
list_operation()