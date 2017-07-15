"""
author: fangren
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for i in range(num+1):
            binary = bin(i)[2:]
            count = sum([int(j)*int(j) for j in binary])
            ans.append(count)
        return ans

solution = Solution()
print solution.countBits(5)