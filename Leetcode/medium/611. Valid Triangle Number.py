"""
author: Fang Ren (SSRL)

7/27/2017
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        count = 0
        nums = sorted(nums)
        k = 0
        for i in range(len(nums)-2):
            k = 0
            for j in range(i+1, len(nums)-1):
                current_sum = nums[i] + nums[j]
                if j < k:
                    count += (k-j)
                    start = k+1
                else:
                    start = j+1
                for k in range(start, len(nums)):
                    if nums[k] >= current_sum:
                        k = k-1
                        break
                count += k-start+1
        return count

solution = Solution()
print solution.triangleNumber([2,3,5,7,8,1,33,13])

