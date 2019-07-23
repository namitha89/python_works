def addTwoNumbers(inp, target):   #n2 time complexity

	for i in range(len(inp)-1):
		for j in range(len(inp)-1):
			res = inp[i] + inp[j+1]
			if(res == target):
				return i,j+1   

def addTwoNumbersDic(inp, target): #nlogn time complexity

	temp = {}
	for t in range(len(inp)-1):
		temp[inp[t]] = t
	# print(temp)
	for i in range(len(inp)-1):
		res = target - inp[i]
		if res in temp:
			print(inp[i])

inp = [1,7,8,6,2]
target = 7
# print(addTwoNumbers(inp, target))
print(addTwoNumbersDic(inp, target))



