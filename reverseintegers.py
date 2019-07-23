def integer_reverse(inta):
   rev = 0
   while( inta != 0 ):
   	# print(inta)
   	remainder = inta%10
   	rev = rev*10+remainder
   	inta /=10
   	
   print(rev)

integer_reverse(1234)	