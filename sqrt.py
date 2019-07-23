def sqrt(n):
	approx = n/2.0
	better = (approx + n/approx) / 2.0
	while better != approx:
		approx = better
		better = (approx + n/approx) / 2.0
		# print(better)
	return approx
print("result is:")
print(sqrt(25))

