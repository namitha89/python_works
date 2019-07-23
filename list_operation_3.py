#Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each.
def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    """
    for i in range(len(u)):
      u[i] +=v[i]
    print(u)

add_vectors([1, 0], [1, 1])
add_vectors([1, 2], [1, 4])
add_vectors([1, 2, 1], [1, 4, 3])
add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
# add_vectors([[1,2,3][4,5,6]],[[5,6,1][8,9,10]])

