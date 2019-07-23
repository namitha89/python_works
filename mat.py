import logging

logging.basicConfig(filename='mathoperation.log',level=logging.INFO)

def logger(func):
	print("Input----------- '{}'".format(func))
	def log_func(*args):
		logging.info("running '{}'".format(func.__name__,args))
		return func(*args)
	return log_func

@logger
def add(x, y):
	return x + y
# add_func = logger(add)  
# add_func(1,2)
@logger
def mul(x, y):
	return x*y

@logger
def pow(x, y):
	return x**y
