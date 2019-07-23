x = "hello this is testing and the logic to test is testing in the hello and color, this is perfect color of the and perfect"
y = x.split(' ')
res = {}
for i in y:
	if i not in res:
		res[i] = 1
	else:
		res[i] += 1

for j in res:
	if(res[j] == 3):
		print(j) 
	
		