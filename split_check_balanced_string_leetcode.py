# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s split it in the maximum amount of balanced strings.
#
# Return the maximum amount of splitted balanced strings
def getcombination(data):
    outdata =[]
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i:j] and data[i:j] not in outdata:
                outdata.append(data[i:j])
    return outdata

def stringCount(s):
    # print(s)
    if(s.count('R') == s.count('L')):
        return True
    return False

data="RLRRLLRLRL"
result = getcombination(data)
total = 0
for i in result:
    if(stringCount(i)):
        total += 1
print(total)


