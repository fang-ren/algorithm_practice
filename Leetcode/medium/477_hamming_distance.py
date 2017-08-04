"""
author: fangren

8/3/2017
"""

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                difference = nums[i]^nums[j]
                ans += int(str(difference), 2)
        return ans

solution = Solution()
print solution.totalHammingDistance([4,14,2])

