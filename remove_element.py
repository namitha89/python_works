def removeElement(nums, val):
    new_nums=[]
    for i in  nums:
        if i != val:
            new_nums.append(i)
    return len(new_nums)



nums=[0,1,2,2,3,0,4,2]
val=2
print(removeElement(nums, val))