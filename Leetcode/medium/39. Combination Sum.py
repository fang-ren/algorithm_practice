"""
author: Fang Ren (SSRL)

7/27/2017
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        for candidate in candidates:
            new_target = target - candidate
            ans.append([candidate] + self.combinationSum(candidates, new_target))

solution= Solution()
nums = [7,6,3,2]
target = 7
print solution.combinationSum(nums, target)