"""
author: fangren

8/3/2017
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random_code node's value.
        :rtype: int
        """
        current = self.head.next
        length = 1
        while current:
            length += 1
            current = current.next
        # if length == 1:
        #     return self.head
        ans = self.head
        step = random.randrange(length)
        while step > 0:
            ans = ans.next
            step -= 1
        return ans


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

obj = Solution(head)
print obj.getRandom()