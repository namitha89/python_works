input = raw_input("please enter string to count --->: ")
inputarray = {}
for letter in input:
	if letter in inputarray:
		inputarray[letter] = inputarray[letter] + 1
	else:
		inputarray[letter] = 1
print(sorted(inputarray.items()))