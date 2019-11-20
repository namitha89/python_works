"""Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions."""
def reverseOnlyLetters(s):
    out = ''
    dict = {}

    for i,v in enumerate(s):
        if v.isalpha():
            out +=v

    rstring = out[::-1]
    print(rstring)
    out = []
    j = 0
    l1 =list(rstring)
    for i in s:
        if i.isalpha():
            out.append(l1.pop(0))
        else:
            out.append(i)

    return ''.join(out)




s = "a-bC-dEf-ghIj"
result = reverseOnlyLetters(s)
print(result)



