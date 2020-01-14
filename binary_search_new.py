def binarySearch(arr,target):
    first = 0
    last = len(arr) - 1
    found = False
    # import pdb;pdb.set_trace()
    while(first<=last and not found):
        mid = (first + last)/2
        if arr[mid] == target:
            found = True
        else:
            if arr[mid] < target:
                first = mid + 1
            else:
                first = mid - 1
    print(found)
    # return found







arr = [-1,0,3,5,9,12]
target = 10
res = binarySearch(arr,target)
print(res)