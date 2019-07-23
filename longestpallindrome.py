def longestPalendrome( str ):
	sequence = 0
	for i in range( len(str) ):
		for j in range( len(str) ):
			strin = str[i:j+i+1]
			# print(strin)
			palind = palindromic( strin )
			# print(palind)
			if(palind == True):
				if(sequence < len(strin)):
					sequence = len(strin)
					# if sequence >=2:
						# print("palindrome----->")
						# print( strin )
					# else:
					# 	print("not palindrome")
	print( sequence )

def palindromic( strin ):
    
    strout = strin[::-1]
    # print( strout )
    if(strin == strout):
    	return True
    else:
    	return False

# palindromic("abc")
str = "xabacdaabaa"
longestPalendrome( str )