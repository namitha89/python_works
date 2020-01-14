out = set()
def getAllPermutations(prev, n, rem):
	if len(prev) == n:
		prev.sort()
		res = reduce((lambda x, y: x * y), prev)
		out.add(res)
		return
	for index, value in enumerate(rem):
		temp = prev[::]
		temp.append(value)
		getAllPermutations(temp, n,rem[0:index]+rem[index+1:])


def maximumProduct(nums):
	nlen = len(nums)
	if nlen < 3:
		return
	if nlen == 3:
		res = reduce((lambda x, y : x * y),nums)
		return res
	else:
		getAllPermutations([], 3, nums)
		if out:
			# print(out)
			return max(out)



nums = [1,2,3,4]
res = maximumProduct(nums)
print(res)