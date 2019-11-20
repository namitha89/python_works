class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(n)
        return int(n[::-1])

solution = Solution()
n = 100111
result = solution.reverseBits(n)
print(result)