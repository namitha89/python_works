class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        print(s)
        # import pdb; pdb.set_trace()
        for roman in range(len(s) - 1):
            # print('edfd')
            if mapping[s[roman]] >= mapping[s[roman + 1]]:
                # print('edfd')
                total += mapping[s[roman]]
            else:
                # print('edfd')
                total -= mapping[s[roman]]
        # print(s[-1])
        total += mapping[s[-1]]
        print(total)

Solution = Solution()
Solution.romanToInt('XVIIL')