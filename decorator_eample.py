import time
def log(filename):
    def inner(func):
        def innermost(*args, **kwargs):
            start = time.time()
            s = func(*args, **kwargs)
            end = time.time()
            with open(filename, "w") as f:
                diff = end-start
                x = [start,end,diff]
                f.write(str(x)+'\n')
            return s
        return innermost
    return inner


@log('myfile1.txt')
def view1(param):
    print(param)

@log('myfile2.txt')
def view2(param_one, times=8):
    for i in range(times):
        print(param_one)


view2('hi am doing good', times=3)