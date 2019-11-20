import sys
import threading
import time
import datetime
t1 = datetime.datetime.now()

class Table(threading.Thread):

	def __init__(self, tname):

		super(Table,self).__init__() 
		self.tname = tname

	def run(self):
		print("Running",self.tname)
		self.create_file()

	def create_file(self):
		time.sleep(1)
		f= open(self.tname + ".txt","w+")
		for i in range(1,11):
			res = int(self.tname) * i
			f.write(" {multiple} * {multiplier} =  {res}\r\n".format( multiple=self.tname, multiplier=i, res = res))
		f.close()



# if __name__ == "__main__":
userfeedargv = sys.argv
userfeedinput = userfeedargv[1:]

if not userfeedinput:
	print("please provide the input to write file")
else :
	for key in userfeedinput:
		tab = Table(key)
		tab.start()
		tab.join()
	print ("Thread has finished")

	t2 = datetime.datetime.now()
	timetaken = t2 - t1
	print("Time taken {time}".format(time = timetaken))
	print("Succesfully file created")
		


