"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
def searchIndexPosition(input,s):
    if s in input:
        print(input.index(s))
    else:
        # print(s)
        for i,v in enumerate(input):
            if v < s and v+1 == s:
                print(input.index(v) + 1)
            elif v > s and v-1 == s:
                if(s == 0 ):
                    print(input.index(v))
                else:
                    print(input.index(v) - 1)





input = [1,3,5,6]
s = 0
searchIndexPosition(input,s)
