def checkAttendence(stri):
    # import pdb;pdb.set_trace()
    acount = 0
    lcount = 0
    for i in range(len(stri)):
        if stri[i] == 'A':
            acount += 1
        if stri[i] == 'L' and stri[i+1] == 'L' and stri[i+2] == 'L':
            lcount = 1
        if acount > 1 or lcount == 1:
            return False
    return True

n = 'PPALLL'
res = checkAttendence(n)
print(res)