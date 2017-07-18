"""
author: fangren
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            #print nums[i], rest
            if (target-nums[i]) in left:
                return [i, left.index(target-nums[i])]
            elif (target-nums[i]) in right:
                return [i, right.index(target-nums[i])+i+1]
        return None

solution = Solution()

nums = [3,3]
target = 6
print solution.twoSum(nums, target)