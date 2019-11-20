# Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums, k):
    num1 = nums[0:-k]
    listlen = len(num1)
    num2 = nums[listlen:]
    num2.extend(num1)
    return num2


nums= [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))