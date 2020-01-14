def find_occurance(a, b):
  a, b = str(a), str(b)
  out = []
  for pos in range(len(b)):
    if(a == b[pos:pos+2]):
      out.append(pos)
  return out
result = find_occurance(53, 1932536753)
print(result)