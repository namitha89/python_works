# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
def sortArrayByParityII(A):
    odd = []
    even = []
    odd = list(filter(lambda x:x%2,A))
    even = list(filter(lambda x:not x%2,A))
    out = []
    even.sort()
    out.extend(even)
    odd.sort()
    out.extend(odd)
    print(out)



A=[3,1,2,4]
sortArrayByParityII(A)