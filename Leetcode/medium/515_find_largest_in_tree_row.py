"""
author: fangren
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        maxs = [root.val]
        current_row = [root]
        while current_row:
            next_row = []
            for node in current_row:
                if node.left != None:
                    next_row.append(node.left)
                if node.right != None:
                    next_row.append(node.right)
            if next_row:
                maximum = max(i.val for i in next_row)
                maxs.append(maximum)
            current_row = next_row
        return maxs

