"""
8/17/2017
Author: Fang Ren
"""

"""
diameter of tree

The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree. 
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameterOfTree(root):
    if not root:
        return 0
    left_diameter = diameterOfTree(root.left)
    right_diameter = diameterOfTree(root.right)
    root_diameter = height(root.left) + height(root.right) + 1
    return max(left_diameter, right_diameter, root_diameter)

root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.right = TreeNode(6)
root.left.left.right.left = TreeNode(10)

print height(root)
print diameterOfTree(root)