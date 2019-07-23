def find2(haystack, needle, start):
    for index,letter in enumerate(haystack[2:]):

        if letter == needle:
            return index + start
    return -1



# print(find2("banana", "a", 2))
print(find2("banana", "n", 3))