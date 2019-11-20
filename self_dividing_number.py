"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""
def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    out =[]
    for i in range(left,right+1):
        num = checkNumberDivedesByItself(i)
        if num:
            out.append(num)
    return out

def checkNumberDivedesByItself(i):
    s = str(i)
    l = len(s)
    if l == 1:
        return i
    else:
        s_list = map(int, s)
        # print(i)
        flag = True
        for x in s_list:
            x = int(x)
            if x == 0:
                flag = False
            elif (i%x) == 0:
                flag = True
            else:
                flag = False
                break
        if flag:
            return i
        else:
            return

left = 1
right = 22
res = selfDividingNumbers(left, right)
print(res)