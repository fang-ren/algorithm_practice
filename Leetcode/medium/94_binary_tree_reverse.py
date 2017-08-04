"""
author: fangren

8/3/2017
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            left = root.left
            right = root.right
            left = self.inorderTraversal(left)
            right = self.inorderTraversal(right)
            root.right = left
            root.left = right
        return root



    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass

solution = Solution()
root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print solution.inorderTraversal(root)