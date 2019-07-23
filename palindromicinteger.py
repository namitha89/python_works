def integer_palindrome(inta):
   rev = 0 
   act = inta
   while( inta != 0 ):
   	# print(inta)
   	remainder = inta%10
   	rev = rev*10+remainder
   	inta /=10
   	
   # print(act)
   if( act == rev):
   	print("number is palindrome")
   else:
   	print("number is not palindrome")

integer_palindrome(121)