def longest_palindromic_substring(str):
    strlen = len(str)
    seqarray = {}
    count = 1
    sequence = 0
    newarray = {}

    for i in range(strlen):
        for j in range(strlen):
            seqstr = str[i:j+1]
            if seqstr not in seqarray:
                seqarray[seqstr] = count
            else:
                seqarray[seqstr] = count + 1
            if seqstr not in newarray and seqstr == seqstr [::-1]:
                newarray[seqstr] = len(seqstr)
                key_max = max(newarray.keys(), key=(lambda k: newarray[k]))

    print(key_max)
longest_palindromic_substring('cbbd')