inputstring = 'hello this is naren and namitha in the woods of sicario and egypt'
print inputstring
res = inputstring.split(' ')
z = []
x = res[:len(res)/2]
y = res[len(res)/2:]
z = y + x
print ' '.join(z)