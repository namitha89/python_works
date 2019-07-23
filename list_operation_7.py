def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """

    for i in range(len(u)):
       u[i] *= v[i]
    print(sum(u))

dot_product([1, 1], [1, 1])
dot_product([1, 2], [1, 4])
dot_product([1, 2, 1], [1, 4, 3])
dot_product([2, 0, -1, 1], [1, 5, 2, 0])

