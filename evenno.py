a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []
for i in a:
    if (i%2) == 0:
        even.append(i)
#print(even)


def getEvenNumber(i):
    if (i%2) == 0:
        return True
x = filter(getEvenNumber, a)
print(x)