# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
def sortArrayByParityII(A):
    odd = []
    even = []
    even = list(filter(lambda x:x%2,A))
    odd = list(filter(lambda x:not x%2,A))
    print(even)
    print(odd)
    out=[]
    for i in range(len(A)):
        if(i%2):
            out.append(even[0])
            even.pop(0)
        else:
            out.append(odd[0])
            odd.pop(0)
    print(out)









n = [4,2,5,7]
sortArrayByParityII(n)