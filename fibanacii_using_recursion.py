
import time

def fib(n):
	if(n==0):
		return 1
	if(n==1):
		return 1
	return fib(n-2) + fib(n-1)


start = time.time()
print(fib(200))

end = time.time()
print("recursion ----- time taken = ", end-start)
