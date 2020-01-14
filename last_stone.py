def last_stone(stones):
	while len(stones) > 1:
		stones.sort()
		x, y = stones[-2],stones[-1]
		stones = stones[:-2]
		if (x!=y):
			stones.append(y-x)
	return stones[0] if stones else 0







arr= [2,7,4,1,8,1]
res = last_stone(arr)
print(res)