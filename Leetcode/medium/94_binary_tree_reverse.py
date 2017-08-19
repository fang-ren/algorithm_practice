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

class TreeTraversal(object):
    def inorderTraversalIterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        current = root
        res = []
        stack = []
        while 1:
            while current:
                stack.append(current)
                current = current.left
            popped = stack.pop()
            res.append(popped.val)
            if popped.right != None:
                current = popped.right
            if not stack and not current:
                return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            self.inorderTraversal(root.left)
            # then print the data of node
            print(root.val)
            # now recur on right child
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            print(root.val)
            self.preorderTraversal(root.left)
            # then print the data of node
            # now recur on right child
            self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # First recur on left child
        if root:
            self.postorderTraversal(root.left)
            # then print the data of node
            # now recur on right child
            self.postorderTraversal(root.right)
            print(root.val)

class TreeFlipping(object):
    def recursionFlipping(self, root):
        if root == None:
            return None
        if root:
            root.left = self.recursionFlipping(root.left)
            root.right = self.recursionFlipping(root.right)
            root.right, root.left = root.left, root.right
        return root

root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.right = TreeNode(6)
root.left.left.right.left = TreeNode(10)

solution = TreeTraversal()
# solution.inorderTraversal(root)
print "Iteratively"
print solution.inorderTraversalIterative(root)
