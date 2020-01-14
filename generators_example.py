# def generateNumber(n):
#     for i in range(1,n+1):
#         yield(i)
import time

def generateNumber(n):
    li = []
    for i in range(1,n+1):
        li.append(i)
    return li

def writeToFile(res):
    f = open("myfiles.txt", "a")

    for i in res:
        f.write(str(i))

    f.close()

n = 10000
res = generateNumber(n)
start = time.time()
writeToFile(res)
end = time.time()
print(end - start)