a
print a[1:1+len(b)]
for i in range(0, len(a) - len(b)+1):
	if a[i:i+len(b)] == b:
		cnt += 1

print cnt 