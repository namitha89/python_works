import mat
import logging

logging.basicConfig(filename='mathoperation.log',level=logging.INFO)

def logger(func):
	def log_func(*args):
		logging.info("running '{}'".format(func.__name__,args))
		print(func(*args))



@logger
mat.add(1,2)

# mat.mul(1,2)
