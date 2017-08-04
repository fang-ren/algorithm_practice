"""
author: Fang Ren (SSRL)

7/27/2017
"""

class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.parent = None
    def returnList(self):
        ans = []
        while self.parent != None:
            ans.append(self.val - self.parent.val)
            self = self.parent
        return ans

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        current_level = [TreeNode(0)]
        leaves = []
        index = 0
        while current_level:
            next_level = []
            for node in current_level:
                for candidate in candidates:
                    if node.parent == None or (candidate >= (node.val - node.parent.val) and node.parent != None):
                        if node.val + candidate < target:
                            new_node = TreeNode(node.val+candidate)
                            new_node.parent = node
                            next_level.append(new_node)
                        elif node.val + candidate == target:
                            new_node = TreeNode(node.val + candidate)
                            new_node.parent = node
                            leaves.append(new_node)
            current_level = next_level
        ans = []
        for leaf in leaves:
            ans.append(leaf.returnList())
        return ans

solution= Solution()
nums = [2,3,6,7]
target = 7
print solution.combinationSum(nums, target)