l=[[1,2],[3,4],[5,6],[7,8],[1,9],[3,9],[1,6],[5,5]]
#l=[[1,2],[1,9],[1,6],[3,4]]
#1:[2,9,6,5]

#{1:2,3:4,5:6,7:8}
#dictlist = dict(l)
#print(dictlist)

output ={}

for i,k in l:
	if i not in output:
		output[i] = [k]

	else:
		output[i].append(k)

print(output)

#expected output
# {1:[2,9,5,1], 3:[4,9],5:[6,5],7:[7,8]}

	