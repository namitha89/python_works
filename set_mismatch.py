# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
def findErrorNums(nums):
    counter = nums[0]
    out = []
    for i in nums:
        if i != counter:
           out.append(i)
           out.append(counter)
           break
        counter +=1

    return out

nums = [1,2,2,4]
res = findErrorNums(nums)
print(res)