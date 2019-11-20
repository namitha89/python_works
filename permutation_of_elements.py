# Print all possible permutations of r elements in a given array of size n
def getcombinations(prev,r,rem):
	if(len(prev) == r):
		print(prev)
		return
	for index,value in enumerate(rem):
		temp = prev[::]
		temp.append(value)
		getcombinations(temp,r,rem[0:index]+rem[index+1:])

arr = [1,2,3,4,5]
r = 2
getcombinations([],r,arr)