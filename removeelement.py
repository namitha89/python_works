def removeElement( arr , ele):

	uniquearra = []
	for i in arr:
		if i != ele:
			uniquearra.append(i)
	print(len(uniquearra))
	print(uniquearra)

arr = [1,0,3,4,3,2,5,0]
removeElement( arr , 3)
