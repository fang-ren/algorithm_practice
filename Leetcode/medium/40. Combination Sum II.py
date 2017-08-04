"""
author: Fang Ren (SSRL)

7/28/2017
"""

class TreeNode(object):
    def __init__(self, v, i):
        self.val = v
        self.index = i
        self.parent = None

    def returnList(self):
        ans = []
        while self.parent != None:
            ans.append(self.val - self.parent.val)
            self = self.parent
        return ans

    def returnIndices(self):
        ans = []
        while self.parent != None:
            ans.append(self.index)
            self = self.parent
        return ans

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        current_level = [TreeNode(0, -1)]
        leaves = []
        while current_level:
            next_level = []
            for node in current_level:
                history = node.returnIndices()
                for i, candidate in enumerate(candidates):
                    if i not in history and i > node.index:
                        if node.parent == None or (candidate >= (node.val - node.parent.val) and node.parent != None):
                            if node.val + candidate < target:
                                new_node = TreeNode(node.val+candidate, i)
                                new_node.parent = node
                                next_level.append(new_node)
                            elif node.val + candidate == target:
                                new_node = TreeNode((node.val + candidate), i)
                                new_node.parent = node
                                leaves.append(new_node)
            current_level = next_level

        ans = []
        for leaf in leaves:
            combi = leaf.returnList()
            if combi not in ans:
                ans.append(combi)
        return ans

solution= Solution()
nums = [10,1,2,7,6,1,5]
nums = [1,1,1,3,3,5]
#nums = [2,1,3,1,4]
#nums = [1, 1, 1, 2]

target = 10
print solution.combinationSum2(nums, target)

# root = TreeNode(0, -1)
# node1 = TreeNode(1, 0)
# node2 = TreeNode(1, 1)
# node1.parent = root
# node2.parent = node1
#
# print node2.returnIndices()