def userinput():
	user1 = raw_input("please enter you name user1:")
	user2 = raw_input("Please enter you name user2:")
	userinput1 = raw_input("{name1},please select the rock,paper or scissors\n".format(name1=user1))
	userinput2 = raw_input("{name2},please select the rock,paper or scissors\n".format(name2=user2))
	return userinput1, userinput2

def game(u1,u2):
	if(u1 == u2):
		print("Tie,play again!!!")
	elif(u1 == 'rock' and u2 == 'scissors' or u1 == 'scissors' and u2 == 'rock'):
		print("rock wins!!!")
	elif(u1 == 'scissors' and u2 == 'paper' or u1 == 'paper' and u2 == 'scissors'):
		print('scissors wins!!')
	elif(u1 == 'paper' and u2 == 'rock' or u1 == 'rock' and u2 == 'paper'):
		print('paper wins!!')
	else:
		print("please select only rock,paper or scissors ")

def ask_game_continue():		
	userchoice = raw_input("Do you want to conntinue yes or no : ")
	if(userchoice == 'yes'):
		return True
	elif(userchoice == 'no'):
		return False
	ask_game_continue()


def game_start():
	print "staring the game"
	while(True):
		userinput1 , userinput2 = userinput()
		game(userinput1, userinput2)
		userchocice = ask_game_continue()
		if userchocice == False:
			break


game_start()