arr = [-1,0,3,5,9,12]
n = len(arr)-1
l = 0
key = 9
def binarySearch(arr,l,r,key):
    if r>=l:
        mid = l+ (r-1)/2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr,l,mid-1,key)
        else:
            return binarySearch(arr,mid+1,r,key)
    else:
        return -1

res = binarySearch(arr,l,n,key)
print(res)