"""
author: fangren
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        ans = nums[:]
        for i in nums:
            if i in count:
                ans.remove(i)
                ans.remove(i)
            else:
                count[i] = 1
        return ans


solution = Solution()

nums = [1,2,1,3,2,5]

print solution.singleNumber(nums)