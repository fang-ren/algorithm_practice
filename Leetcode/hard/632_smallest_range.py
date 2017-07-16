"""
author: fangren
"""
import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closest_num(self, L, k):
        if not L:
            return []
        L = np.array(L)
        min_difference = min(abs(L-k))
        #print min_difference
        ans = []
        for i in L:
            if abs(i - k) == min_difference:
                ans.append(i)
        return ans

    def smallRange(self, num):
        return range(min(num))


    def tree_to_lists(self, root):
        if root.left == None and root.right == None:
            return [[root.val]]
        lists = []
        if root.left != None:
            left_lists = self.tree_to_lists(root.left)
            for left_list in left_lists:
                lists.append([root.val] + left_list)
        if root.right != None:
            right_lists = self.tree_to_lists(root.right)
            for right_list in right_lists:
                lists.append([root.val] + right_list)
        return lists


    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        lengths = []
        for i in nums:
            lengths.append(len(i))
        small_list = nums[lengths.index(min(lengths))]
        del nums[lengths.index(min(lengths))]
        roots = []
        #print small_list, nums
        for elem in small_list:
            root = TreeNode(elem)
            current_level = [root]
            for other_list in nums:
                #print elem, other_list
                closestNum = self.closest_num(other_list, elem)
                #print closestNum
                next_level = []
                for node in current_level:
                    if len(closestNum) == 1:
                        node.left = TreeNode(closestNum[0])
                        next_level.append(node.left)
                    if len(closestNum) == 2:
                        node.left = TreeNode(closestNum[0])
                        node.right = TreeNode(closestNum[1])
                        next_level.append(node.left)
                        next_level.append(node.right)
                current_level = next_level
            #print self.tree_to_lists(root)
            roots.append(root)
        lists = self.tree_to_lists(root)
        #print min(lists[0]), max(lists[0])
        smallest_range = range(min(lists[0]), max(lists[0]))
        for root in roots:
            lists = self.tree_to_lists(root)
            for num in lists:
                #print len(smallest_range)
                #print num
                if min(num) == max(num):
                    return [min(num), max(num)]
                else:
                    current_range = range(min(num), max(num))
                    if len(current_range) < len(smallest_range):
                        smallest_range = current_range
                    if len(current_range) == len(smallest_range) and min(current_range) < min(smallest_range):
                        smallest_range = current_range
        return [min(smallest_range), max(smallest_range)+1]

solution = Solution()
# L = [4,10,15,24,26]
# k = 0
# print solution.closest_num(L, k)
# #
#nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# nums = [[1,2,3],[1,2,3],[1,2,3]]
# nums = [[1,3,5,7,9],[2,4,6,8,10]]
nums = [[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]
print solution.smallestRange(nums)


# node1 = TreeNode(15)
# node2 = TreeNode(7)
# node3 = TreeNode(20)
# node5 = TreeNode(10)
# node3.left = node1
# node3.right = node2
# node4 = TreeNode(9)
# node4.right = node5
# root = TreeNode(3)
# root.left = node4
# root.right = node3
#
# print solution.tree_to_lists(root)