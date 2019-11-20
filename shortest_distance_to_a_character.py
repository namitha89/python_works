# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
def shortestToChar(s,c):
    right_index = getDistanceIndex(s[::-1])
    right_index.reverse()
    left_index = getDistanceIndex(s)
    res = []
    for i in range(len(s)):
        data = min(left_index[i],right_index[i])
        res.append(data)
    return res

def getDistanceIndex(s):
    out = []
    for i in range(len(s)):
        str = s[i:]
        res = str.find(c)
        if(res == -1):
            out.append(99999)
        else:
            out.append(res)
    return out


s = "loveleetcode"
c = 'e'
result_array=shortestToChar(s, c)
print(result_array)