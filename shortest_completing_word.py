# Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

# The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.
def shortestCompletingWord(licensePlate, words):
    out = {}
    flag = True

    for i in words:
        count = 1
        var = i
        for x,j in enumerate(licensePlate):
            if j in var:
                var1 = var.find(j)
                if var1 == -1:
                    break
                else:
                    var = remove_char(var, var1)
                    flag = True
            else:
                flag = False
                break
        if flag:
            value = len(i)
            out[i] = value
    temp = min(out.values())
    res = [key for key in out if out[key] == temp]
    if(res):
        return res[0]
    else:
        return

def remove_char(str, n):
    strreplaced = str.replace(str[n],"",1)
    return strreplaced

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
licensePlate = ''.join([ c for c in licensePlate if c.isalpha()])
strlicense = licensePlate.lower()
result = shortestCompletingWord(strlicense, words)
print(result)