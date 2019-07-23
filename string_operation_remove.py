def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    word = s.replace(sub,'',1)
    print(word)

def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    word = s.replace(sub,'')
    print(word)

if __name__ == '__main__':
    import doctest
    print doctest.__file__
    doctest.testmod()

remove('an', 'banana')
remove('cyc', 'bicycle')
remove('iss', 'Mississippi')
remove('egg', 'bicycle')

remove_all('an', 'banana')
remove_all('cyc', 'bicycle')
remove_all('iss', 'Mississippi')
remove_all('eggs', 'bicycle')