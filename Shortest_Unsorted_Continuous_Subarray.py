# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

def findUnsortedSubarray(nums):
    l = len(nums)
    r = 0
    for i in range(l-1):
        for j in range(i+1,l):
            print(j)
            if nums[j] < nums[i]:
                r = max(r,j)
                l = min(l,i)
    if r - l < 0:
        return 0
    else:
        return r-l+1






nums = [2, 6, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(nums))