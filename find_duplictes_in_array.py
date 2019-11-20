def remove_duplicates(inputlist):
    diclist = {}
    single = []
    for i in inputlist:
        if i not in diclist:
            diclist[i] = 1
        else:
            diclist[i] +=1

    print(diclist)
    for key,value in diclist.items():
        if value == 1:
            single.append(key)

    print(single)



inputlist = [1,3,3,5,9,4,1,10,9,7,2,7]
remove_duplicates(inputlist)