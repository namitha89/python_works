inputstring = 'ab1c54'
s = 0
for i in inputstring:
	if(i.isnumeric):
		s = s+int(i)
print s