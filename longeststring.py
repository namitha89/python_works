def longestSubString( str ):
	strlen = len( str )
	arr = []
	longest = 1
	sequence = 0 
	for x in range(strlen):
	  for y in  range(strlen):
	  	seqstring = str[x:y+1]
	  	
	  	norepeat = norepeatingCharacters( seqstring )
	  	if( norepeat == True):
	  		if(sequence < len( seqstring )):
	  			sequence = len( seqstring )
	  		else:
	  			sequence = sequence
	print(sequence)

	


def norepeatingCharacters( inputstring ):
	keycheck = {}
	for i in inputstring:
	  if i not in keycheck:
	    keycheck[i] = ''
	    print(keycheck)
	  else:
	   	return False
	return True
	  

str = "abcabcjkt"




def unittest():
	assert norepeatingCharacters('abc') == True , "norepeatingCharacters didnot return true"
	assert norepeatingCharacters('abca') == False , "norepeatingCharacters didnot return False"

unittest()