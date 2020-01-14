def getPrimeNumber(n):
    li = []
    for i in range(n+1):
        if i%2 != 0:
            li.append(i)
    return li
res = getPrimeNumber(5)
# print(res)

def getAllPermutations(prev, n, rem):
    if (len(prev) == n):
        print(prev)
        return
    for index, value in enumerate(rem):
        temp = prev[::]
        temp.append(value)
        getAllPermutations(temp, n , rem[0:index] + rem[index + 1:])

getAllPermutations([],len(res),res)

