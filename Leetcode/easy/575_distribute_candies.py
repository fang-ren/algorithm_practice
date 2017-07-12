"""
author: fangren
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        import numpy as np
        kinds = np.unique(candies)
        return min(len(kinds), len(candies)/2)


solution = Solution()
print solution.distributeCandies([1,1,2,2,3,3])