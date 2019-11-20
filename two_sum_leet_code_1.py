def two_numbers(nums,target):
    dict_nums = {nums[i] : i for i in range(0,len(nums))}
    seen = {}
    for i,num in enumerate(nums):
        remaining = target - num
        if remaining in dict_nums:
            return dict_nums[num],dict_nums[remaining]
    return []




nums = [1,8,3,4,2,6]
target = 5
print(two_numbers(nums,target))