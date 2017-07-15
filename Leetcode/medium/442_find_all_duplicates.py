"""
author: fangren
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        ans = []
        for elem in dict:
            if dict[elem] == 2:
                ans.append(elem)
        return ans

solution = Solution()
print solution.findDuplicates([4,3,2,7,8,2,3,1])