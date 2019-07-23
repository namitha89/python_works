import time

def fib(n):
	x , y  = 1,1
	print(x)

	for i in range(n):
		x,y = y ,x+y
		print(x)

start = time.time()
print(fib(200))

end = time.time()
print("for loop ----- time taken = ", end-start)