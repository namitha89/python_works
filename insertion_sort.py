def insertionSort(alist):
    # import pdb;pdb.set_trace()
    for i in range(1,len(alist)):
        curr = alist[i]
        # print(curr)
        for x in range(i-1,0,-1):
            if alist[x] > curr:
                alist[x+1] = alist[x]
            else:
                alist[x+1] = curr
                break


print(insertionSort([5,2,1,9,0,4,6]))