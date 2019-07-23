def count_character(n,chname):
  fruit = n
  count = 0
  for char in fruit:
    if char == chname:
      count += 1
  print count

count_character("banana","b")