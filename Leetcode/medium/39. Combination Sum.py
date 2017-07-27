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
        if target < min(candidates):
            return
        if target == min(candidates):
            return [target]
        ans = []
        for candidate in candidates:
            new_target = target - candidate
            if target > 0:
                ans.append([candidate]+ self.combinationSum(candidates, new_target))
        return ans

solution= Solution()
nums = [2,3,6,7]
target = 7
print solution.combinationSum(nums, target)