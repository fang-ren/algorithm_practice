"""
author: fangren
"""

class Solution(object):
    def residual(self, nums, target):
        ans = sum([abs(num - target) for num in nums])
        return ans

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: intx
        """
        nums = sorted(nums)
        if len(nums) %2 == 0:
            median = (nums[len(nums)/2-1] + nums[len(nums)/2])/2
        else:
            median = nums[len(nums)/2]
        min_move = self.residual(nums, median)
        return min_move



solution = Solution()
nums = [1,2,3]
print solution.minMoves2(nums)
#  print solution.residual(nums, 3)