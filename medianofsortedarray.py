import decimal
def calculateMedian(listone, listtwo):
	mergedlist = listone + listtwo
	median = len(mergedlist)
	medpos = float(median/2)
	# print(median)
	if(medpos%2 == 0.0):
		pos = int(medpos)
		return mergedlist[pos]
	else:
		fistmid = int(medpos)
		# print(fistmid)
		medelment = mergedlist[fistmid-1] + mergedlist[fistmid]
		actaulmid = decimal.Decimal(medelment)/decimal.Decimal(2)
		return actaulmid
		


	
	


actuallva = calculateMedian([1,2,3], [4,5,6])
print(actuallva)
