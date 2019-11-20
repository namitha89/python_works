# Return the smallest possible difference between the maximum value of B and the minimum value of B
def smallestRangeI(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    if not A:
        return 0
    out =[]
    min_value = A[0]
    max_value = A[0]
    for x in  range(len(A)):
        min_value = min(min_value,A[x])
        max_value = max(max_value,A[x])
    answer = (max_value - min_value) - 2*K
    if answer < 0:
        return 0
    return  answer



A = [1,3,6]
K = 3
resu = smallestRangeI(A,K)
print(resu)
