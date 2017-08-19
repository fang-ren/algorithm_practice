"""
8/16/2017
Author: Fang Ren
"""

"""
Change a binary tree to a circular double linked list
"""

class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class DoubleLinkedList():
    def __init__(self, value):
        self.val = value
        self.previous = None
        self.next = None

def TreeToList(root):
    # use inorder tree traversal
    if root == None:
        return []
    current = root
    stack = []
    popped = None
    index = 1
    while index:
        while current:
            stack.append(current)
            current = current.right
        old_popped = popped
        popped = stack.pop()
        popped.next = old_popped
        old_popped.previous = popped
        if index == 1:
            tail = popped # only store once
            index += 1
        if popped.right != None:
            current = popped.right
        if not stack and not current:
            # connect tail to head
            popped.previous = tail
            tail.next = popped
            return popped






