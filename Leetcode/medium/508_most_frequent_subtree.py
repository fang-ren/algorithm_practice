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
    def treeSum(self, root):
        if root.left == None and root.right == None:
            return root.val
        ans = root.val
        if root.left != None:
            ans += self.treeSum(root.left)
        if root.right != None:
            ans += self.treeSum(root.right)
        return ans
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        dict = {}
        current_level = [root]
        while current_level:
            next_level = []
            for node in current_level:
                sum = self.treeSum(node)
                if sum in dict:
                    dict[sum] += 1
                else:
                    dict[sum] = 1
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            current_level = next_level
        max_frequency = max(dict.values())
        ans = []
        for key in dict:
            if dict[key] == max_frequency:
                ans.append(key)
        return ans


node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20)
node3.left = node1
node3.right = node2
node4 = TreeNode(9)
root = TreeNode(3)
root.left = node4
root.right = node3

solution = Solution()
print solution.findFrequentTreeSum(root)