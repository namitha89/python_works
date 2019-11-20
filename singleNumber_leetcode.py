# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def singleNumber(n):
    dict_data ={}
    for i in n:
        if i in dict_data:
            dict_data[i] +=1
        else:
            dict_data[i] = 1
    # for x, y in dict_data.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    #     if y == 1:
    #         print(x)
    dict1_keys = {x for x,y in dict_data.items() if y == 1}
    print(dict1_keys)


n=[4,1,2,1,2]
singleNumber(n)
