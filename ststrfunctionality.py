def findstringoccurence( str, wrd):
    n = len(wrd)
    for i in range(len(str)):
		for j in range(len(str)):
		  if(wrd == str[i:j+1]):
		  	return i
    return -1	



sequence = findstringoccurence( "kjflkjdslaariu" , "aa")
print(sequence)