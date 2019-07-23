def count(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    # count = s.count(sub)
    # print(count)
    count = 0
    for i in range(len(s)):
      if s[i:i+len(sub)] == sub:
        count += 1
    print(count)

      

count('is', 'Mississippi')
count('ana', 'banana')
count('nana', 'banana')
count('nanan', 'banana')