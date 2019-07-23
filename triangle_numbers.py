def print_triangle_numbers(n):
  number = 0

  print("The first {} triangular numbers are...").format(n)
  for i in range(1,5):
    number = number + i
    print(number)



print_triangle_numbers(5)