
def sample_generator():
    i = 0
    while i < 4:
        print("here")
        # print("yielding {res}".format(res=i))
        yield i
        i = i+1
        print("i am herrrr ")




#--------------------------------

uu = sample_generator()

import pdb;pdb.set_trace()

for i in uu:
    print("time elapsed {}".format(i))