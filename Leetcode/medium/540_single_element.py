"""
author: fangren
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return None
        while nums:
            if len(nums) == 1:
                return nums[0]
            if nums[0] != nums[1]:
                return nums[0]
            else:
                del nums[0]
                del nums[0]

solution = Solution()
A =[1,1,2,3,3,4,4,8,8]
A = [3,3,7,7,10,11,11]
#A = [1]
print solution.singleNonDuplicate(A)