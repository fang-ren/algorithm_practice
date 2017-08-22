"""
8/18/2017
Author: Fang Ren
"""

"""
flatten a linked list
"""

class LinkedList():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.child = None

def flattenLinkedList(head):
    pre_head = LinkedList(0)
    pre_head.child = head
    current_level = [pre_head]
    flattenedList = []
    while current_level:
        next_level = []
        for node in current_level:
            childNode = node.child
            while childNode:
                next_level.append(childNode)
                childNode = childNode.next
        current_level = next_level
        flattenedList += [currentNode.val for currentNode in current_level]
    return flattenedList


head = LinkedList(10)
head.child = LinkedList(4)
head.child.next = LinkedList(20)
head.next = LinkedList(5)
head.next.next = LinkedList(12)

print flattenLinkedList(head)



