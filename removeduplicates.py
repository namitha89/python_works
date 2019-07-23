def compute(names) :
	return list(set(names))

def compute2(names) :
	y = []
	for i in names :
		if i not in y :
			y.append(i)
	return y

names = ["Michele", "Robin", "Sara", "Michele"]
print(names)


print(compute(names))

print(compute2(names))