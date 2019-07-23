#Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s.
def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    for i in range(len(v)):
    	v[i] = s * v[i]
    
    print(v)
scalar_mult(5, [1, 2])
scalar_mult(3, [1, 0, -1])
scalar_mult(7, [3, 0, 5, 11, 2])
