# def reverse(s):
#     """
#       >>> reverse('happy')
#       'yppah'
#       >>> reverse('Python')
#       'nohtyP'
#       >>> reverse("")
#       ''
#       >>> reverse("P")
#       'P'
#     """
#     y = ''
#     for i in s[::-1]:
#       y = y + i
#     print(y)

# def mirror(s):
#   """
#       >>> mirror("good")
#       'gooddoog'
#       >>> mirror("yes")
#       'yessey'
#       >>> mirror('Python')
#       'PythonnohtyP'
#       >>> mirror("")
#       ''
#       >>> mirror("a")
#       'aa'
#     """
  # y = ''
  # for i in s[::-1]:
  #   y = y + i
  # print(s+y)

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    word = ''
    for i in strng:
      if (i == letter):
        word = word + ''
      else:
        word = word + i
    print(word)
  




if __name__ == '__main__':
    import doctest
    doctest.testmod()

# reverse('happy')
# reverse('Python')
# reverse("")
# reverse("P")
# mirror("good")
# mirror("yes")
# mirror('Python')
# mirror("")
# mirror("a")
remove_letter('a', 'apple')
remove_letter('a', 'banana')
remove_letter('z', 'banana')
remove_letter('i', 'Mississippi')
