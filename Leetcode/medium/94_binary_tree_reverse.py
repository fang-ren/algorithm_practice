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

class TreeWalk(object):
    def inorderWalk(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            self.inorderWalk(root.left)
            # then print the data of node
            print(root.val)
            # now recur on right child
            self.inorderWalk(root.right)

    def preorderWalk(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            print(root.val)
            self.preorderWalk(root.left)
            # then print the data of node
            # now recur on right child
            self.preorderWalk(root.right)

    def postorderWalk(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            self.postorderWalk(root.left)
            # then print the data of node
            # now recur on right child
            self.postorderWalk(root.right)
            print(root.val)

class Solution(object):
    def recursionTransversal(self, root):
        if root:
            root.right, root.left = self.inorderTraversal(root.left), self.inorderTraversal(root.right)
        return root

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pass


root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
