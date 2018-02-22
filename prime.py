#!/usr/bin/python

def primecheck( num ):
	print "check {} is prime or not".format(num)
	if (( num % 2) == 0):
		print "Given number is not a prime number"
	else:
		print "Given number is prime number"

	return;

primecheck(17)


ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print ans