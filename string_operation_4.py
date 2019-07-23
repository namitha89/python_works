inp = "abjkisdjkiss"
sub = "jki"

found = ""

for i, c in enumerate(inp):
  if not (sub == inp[i:len(sub)+i]):
    found += c
  else:
  	found += inp[len(sub)+i:]
  	break

print(found)