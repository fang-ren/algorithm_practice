"""
author: fangren
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0)+1
        for val in dict:
            if dict[val] == 1:
                return val

solution = Solution()
print solution.singleNumber([-1])