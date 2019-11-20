# Print all possible permutations of r elements in a given array of size n

output = []

def getcombinations(prev, rem):
    if len(prev) == r:
        output.append(sorted(prev))
        return

    for index,value in enumerate(rem):
        temp = prev[::]
        temp.append(value)
        getcombinations(temp, rem[0:index]+rem[index+1:])

arr = [1,2,3,4,5]
r = 2
getcombinations([], arr)
print(list(set(output)))