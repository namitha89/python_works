f = open('nami.txt','a+')
for i in range(10):
    f.write("Append this is the line no %d\r\n" %(i+1))

f.close()

