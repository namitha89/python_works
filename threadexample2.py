# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 

import  time

def print_time(): 
	""" 
	function to print cube of given num 
	"""
	for i in range(5):
		print(time.time())
		time.sleep(1)

def counter(): 
	""" 
	function to print square of given num 
	"""
	x = 0
	for i in range(10):
		x += 1
		print(x)
		time.sleep(1)


if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=counter) 
    t2 = threading.Thread(target=print_time) 

	# starting thread 1 
    t1.start() 
	# starting thread 2 
    t2.start() 

	# wait until thread 1 is completely executed 
    t1.join() 
	# wait until thread 2 is completely executed 
    t2.join() 

	# # both threads completely executed 
    print("Done!") 
