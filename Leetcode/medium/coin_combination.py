"""
author: fangren
"""

class Solution(object):
    def combination(self, nums, target):
        if target < 0:
            return []
        if target == 0:
            return [[]]
        changes = []
        for num in nums:
            sub_changes = self.combination(nums, target - num)
            for combo in sub_changes:
                combo.append(num)
                changes.append(combo)
        return changes

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = self.combination(nums, target)
        print ans
        print len(ans)
        return ans

solution = Solution()
ans = solution.combination([1,2,3], 4)
print ans