class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        result = reduce(lambda x,y:int(x)+int(y),n)
        return result

solution = Solution()
n = 10011111111111111111111111111111111111
result = solution.hammingWeight(n)
print(result)