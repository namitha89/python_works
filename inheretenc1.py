x=0
class fruits:

   def __init__(self):

   	global x
   	x+=1
   	print("I am a fruit")

class citrus:

	def __init__(self):
		super().__init__()
		global x
		x+=2
		print("I'm citrus")

lime=citrus()
