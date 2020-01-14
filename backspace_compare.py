def backspaceCompare(s, t):
	newstr_s = ''
	newstr_t = ''
	slist = list(s)
	tlist = list(t)
	# import pdb;pdb.set_trace()
	for i,value in enumerate(slist):
		if value =='#':
			if (slist[i - 1]):
				slist[i - 1] = ''
			slist[i] = ''
		elif value == '#' and i == 0:
			slist[i] = ''

	for i,value in enumerate(tlist):
		if value =='#'and i !=0:
			if(tlist[i-1]):
				tlist[i-1] = ''
			tlist[i] = ''
		elif value == '#' and i == 0:
			tlist[i] = ''

	newstr_s = newstr_s.join(slist)
	newstr_t = newstr_t.join(tlist)
	if newstr_s == newstr_t:
		return True
	if len(newstr_s) == 0 and len(newstr_s) == 0:
		return True
	else:
		return False


s='a##c'
t="#a#c"
compared = backspaceCompare(s, t)
print(compared)