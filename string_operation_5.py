# inp = "Mississippi"
# sub = "iss"

# found = []
# found_res = ''

# i = 0
# while ( i<len(inp) ):
# 	# import pdb;pdb.set_trace()
# 	word = inp[i:len(sub)+i]
# 	if(sub != word):
# 		found_res +=inp[i]
# 		i += 1
# 	else:
# 		i += len(sub)
# print(found_res)

	
inp = "Mississippi"
sub = "iss"

found = []
found_res = ''
# for i, c in enumerate(inp):
# 	word = inp[i:len(sub)+i]
# 	if(word != sub):
# 		found_res += c
# 	else:
i = 0
for x in range(len(inp)):
	# import pdb;pdb.set_trace()
	word = inp[i:len(sub)+i]
	if(sub != word):
		found_res +=inp[i]
		i += 1
	else:
		i += len(sub)







print(found_res)

	






 

    




      








 

    




      


