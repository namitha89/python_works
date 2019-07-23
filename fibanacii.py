# 1,1,2,3,5,8,13,21,34,55

def printfibnacii(n):
	first = 1
	second = 1
	i = 0
	listfib = []
	listfib.append(first)
	listfib.append(second)
	while i < n:
		third = first + second
		first = second
		second = third
		listfib.append(third)
		i = i+1
	return listfib

def fib(n):
	if(n <= 1):
		return n
	else:
	  return fib(n-1) + fib(n-2)
	  
for i in range(5):
	print(fib(i))

	

# print(fib(5))
