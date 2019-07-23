num = int(input("provide the number to check the num :"))
check = int(input("provide the number to divide by :"))

if num % 4 == 0:
	print(num, "The given number divides by 4")

elif num % 2 == 0:
	print(num, "the given num is even")
else:
	print(num,"the given num is odd")

if num % check == 0:
	print(num,"num divide evenly",check)
else:
	print(num,"doesnot divide evenly",check)
