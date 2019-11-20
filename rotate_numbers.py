"""X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?"""
dict = {
        1:1,
        2:5,
        3:'',
        4:'',
        5:2,
        6:9,
        7:'',
        8:8,
        9:6,
        10:10

    }

def rotateNumbers(n,dict):
    out = []
    for i in range(1,n+1):
        # print(i)
        val = get_value(i)
        if val:
            out.append(val)
    return len(out)

def get_value(val):
    for key, value in dict.items():
        if val == value and key != value:
            return value
    return





n = 10
res = rotateNumbers(n,dict)
print(res)
