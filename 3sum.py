def triplesum(inp_array):
    inp_len = len(inp_array)
    sum = 0
    res = []
    out = []


    for i in range(inp_len):
        for j in range(inp_len-1):
            for k in range(inp_len-2):
                sum_three = inp_array[i] + inp_array[j+1] + inp_array[k+2]
                if sum_three == sum:
                    list = [inp_array[i],inp_array[j+1],inp_array[k+2]]
                    list.sort()
                    # print(list)
                    out.append(list)
    Output = set([tuple(i) for i in out])
    return Output










print(triplesum([-1, 0, 1, 2, -1, -4]))