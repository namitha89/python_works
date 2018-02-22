def is_prime(number):
	prime = True
	for num in range(2,number):

		if not (number % num):
			prime = False

		if not prime:
			print "Not a prime"
			return 

	print "is a prime"

is_prime(6)
