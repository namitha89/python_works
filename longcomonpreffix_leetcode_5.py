input_arr = ["flower","fl","flight"]

# # find minimum number

print(min(map(len, input_arr)))

# #find the prefix

input_arr = ["flower","flow","flight"]
prefix=[]
temp = ''
for i in range(min):
    for index, ele in enumerate(input_arr):
        if i < len(ele):
            if index == 0:
                temp = ele[i]
            if temp !=ele[i]:
                break
        else:
            break

    prefix.append(temp)


result_pre = ''.join(map(str, prefix))
print(result_pre)