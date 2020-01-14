def maximumSumArray(l, k):
    l.sort()
    res=[]
    k =k-1
    for i in range(len(l)):
        if i < k:
            if l[i] == 0:
                s = sum(l)
                res.append(s)
                break
            l[i]= - l[i]
            s = sum(l)
            res.append(s)
    if res:
        res = max(res)
    return res


l = [9, 8, 8, 5]
k=3
res = maximumSumArray(l, k)
print(res)