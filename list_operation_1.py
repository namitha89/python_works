#Write a loop that traverses:
#and prints the length of each element. What happens if you send an integer to len? Change 1 to 'one' and run your solution again.
def display_list(l):
  for index,value in enumerate(l):
  	print(len(value))
	

listeaxpl = ['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

display_list(listeaxpl)

