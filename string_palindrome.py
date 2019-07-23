def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    pal = ''
    for i in s[::-1]:
      pal = pal + i;
    if pal == s:
      print(True)
    else:
      print(False)

is_palindrome('abba')
is_palindrome('abab')
is_palindrome('tenet')
is_palindrome('banana')
is_palindrome('straw warts')
