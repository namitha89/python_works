# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
def reverseStr(s, k):
	newstr = ''
	index = 2
	out = []
	for i in xrange(0, len(s), k):
		op = s[i:i + k]
		out.append(op)
	for i,value in enumerate(out):
		if i%2 == 0:
			newstr += value[::-1]
		else:
			newstr += value
	print(newstr)





s = 'abcdefgh'
k =2
reverseStr(s, k)