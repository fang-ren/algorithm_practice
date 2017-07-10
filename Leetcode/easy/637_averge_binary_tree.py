# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20)
node3.left = node1
node3.right = node2
node4 = TreeNode(9)
root = TreeNode(3)
root.left = node4
root.right = node3


import numpy as np

class Solution():
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        averages = [root.val]
        current_level = [root]
        while current_level:
            # print current_level
            next_level = []
            sum = 0
            for node in current_level:
                #print node.left != None, node.right != None
                if node.left != None:
                    next_level.append(node.left)
                    sum += node.left.val
                if node.right != None:
                    next_level.append(node.right)
                    sum += node.right.val
            if next_level:
                average = sum/float(len(next_level))
                current_level = next_level
                averages.append(average)
            else:
                current_level = []
        return averages


solution = Solution()
ans = solution.averageOfLevels(root)
print ans