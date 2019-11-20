import time

def logging(func):

    def inner(arg):
        begin = time.time()
        result =  func(arg)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return result
    return inner

@logging
def somefunction(argv):
    time.sleep(2)
    print(argv)


somefunction(10)