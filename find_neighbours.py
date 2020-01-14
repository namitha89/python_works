def find_neighbours(newarr, r, c):
	clen = len(newarr[0])
	rlen = len(newarr)
	if r < 0 and r >= rlen:
		return
	if c < 0 and c >= clen:
		return
	return [[r, c+1],[r, c-1],[r-1, c],[r-1, c+1],[r-1, c-1],[r+1, c-1],[r+1, c],[r+1,c+1]]




points=[0,0]
r = points[0]
c = points[1]
newarr = [
	[1, 0, 1, 1],
	[1, 1, 0, 0],
	[0, 0, 1, 1],
	[1, 0, 1, 0]
]
res = find_neighbours(newarr, r, c)
print(res)