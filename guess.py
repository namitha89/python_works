import random

number_rand = random.randint(1,9)
count = 0;
guess = 0;
while(guess != number_rand and guess != 'exit'):
	guess = raw_input("please enter number:");
	guess = int(guess)
	count +=1;
	if( number_rand < guess):
		print("The given input is high")
		
	elif( number_rand > guess):
		print("The given input is low")
		
	else:
		print("The given input matches hurray!!!",count,"times you tried to guess")
	