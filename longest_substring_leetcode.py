def longestSubString(str):
    strlen = len(str)
    arr = {}
    sequence = 0
    count = 1
    # import pdb; pdb.set_trace()
    for x in range(strlen):
        for y in range(strlen):
            seqstring = str[x:y + 1]

            norepeat = norepeatingCharacters(seqstring)
            if (norepeat == True):
                if seqstring not in arr:
                    arr[seqstring] = count
                else:
                    arr[seqstring] = count + 1

                if (sequence < len(seqstring)):
                    sequence = len(seqstring)
                else:
                    sequence = sequence


    print(sequence)


def norepeatingCharacters(inputstring):
    keycheck = {}
    for i in inputstring:
        if i not in keycheck:
            keycheck[i] = ''
            # print(keycheck)
        else:
            return False
    return True


str = "abcabcbb"
longestSubString(str)
