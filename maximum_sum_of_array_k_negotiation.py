# Maximize Sum Of Array After K Negations
arr = [2,-3,-1,5,-4]
k=2
res = {}
arr.sort()
# print(arr)
for i in range(0,k):
    for j in range(len(arr)-1):
        arr[j] = arr[j] * -1
        Sum = sum(arr)
        res[j] = Sum
        print(res[j])
print(res)
