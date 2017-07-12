"""
author: fangren
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(findNums)):
            num = findNums[i]
            found = False
            for j in nums[i+1:]:
                if j > num:
                    ans.append(nums.index(j))
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
