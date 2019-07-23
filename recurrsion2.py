def display_single_list(l,resarray):
 
  
  for i in l:
    # print(i)
	if type(i) is list:
		
		# for j in i:
		# 	# print('i am here')
		# 	resarray.append(j)
		display_single_list(i,resarray)

	else:
		# print('nhgj')
		resarray.append(i)

resarray = []
l = [[1,2,3],9,[1,2],1,3,[[9]],6]
display_single_list(l,resarray)
print(resarray)