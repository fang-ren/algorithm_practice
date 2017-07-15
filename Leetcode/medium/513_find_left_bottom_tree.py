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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None:
            return root.val
        layer = [root]
        layers = [layer]
        while layer:
            current_layer = []
            for node in layer:
                if node.left != None:
                    current_layer.append(node.left)
                if node.right != None:
                    current_layer.append(node.right)
            layers.append(current_layer)
            layer = current_layer
        return layers[-2][0].val

solution = Solution()
left = TreeNode(4)
root = TreeNode(5)
root.left = left
print solution.findBottomLeftValue(root)