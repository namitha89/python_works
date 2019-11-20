 # Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate(A, B):
    if A and B:
        for i in range(len(A)):
            str1 = B[0:-i]
            b_len = len(str1)
            str2 = B[b_len:]
            str3 = str2 + str1
            if(str3 == A):
                return True
        return False
    else:
        return True

A = 'abcde'
B = 'abced'
# B = 'cdeab'
print(rotate(A, B))