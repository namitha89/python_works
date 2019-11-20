def reverseWords(s):
    if s:
        l1 = s.split(' ')
        out = []
        for i in l1:
            out.append(i[::-1])
        return " ".join(out)
    else:
        return s

s ="Let's take LeetCode contest"
print(reverseWords(s))