def removeDuplicates( arr ):
	uniqueele = []
	for i in arr:
		if i not in uniqueele:
			uniqueele.append( i )

	print( uniqueele )

i =[0,0,1,1,2,2,3,4,5]
removeDuplicates( i )	
