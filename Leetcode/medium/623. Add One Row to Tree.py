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
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            root, root.left = TreeNode(v),root
            return root
        layer = 1
        current_layer = [root]
        while layer < d-1:
            next_layer = []
            for node in current_layer:
                if node.left != None:
                    next_layer.append(node.left)
                if node.right != None:
                    next_layer.append(node.right)
            current_layer = next_layer
            layer += 1
        for node in current_layer:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return root

    def printTree(self, root):
        current_layer = [root]
        while current_layer:
            next_layer = []
            for node in current_layer:
                print node.val
                if node.left != None:
                    next_layer.append(node.left)
                if node.right != None:
                    next_layer.append(node.right)
            current_layer = next_layer


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

solution = Solution()
root = solution.addOneRow(root, 1, 2)
print solution.printTree(root)