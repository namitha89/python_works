def sum_of_squares_of_digits(n):
    """
      >>> sum_of_squares_of_digits(1)
      1
      >>> sum_of_squares_of_digits(9)
      81
      >>> sum_of_squares_of_digits(11)
      2
      >>> sum_of_squares_of_digits(121)
      6
      >>> sum_of_squares_of_digits(987)
      194
    """
    sum = 0 ;
    for i in str(n):
      sqr = int(i) * int(i)
      sum = sum + sqr;
    print(sum)

if __name__ == '__main__':
  import doctest
  doctest.testmod()

sum_of_squares_of_digits(1)
sum_of_squares_of_digits(9)
sum_of_squares_of_digits(11)
sum_of_squares_of_digits(121)
sum_of_squares_of_digits(987)


