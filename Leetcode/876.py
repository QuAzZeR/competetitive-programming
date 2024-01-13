from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node is not None:
            node = node.next
            count += 1
        middle = count//2 + 1
        node = head
        count = 1
        while node is not None:
            if count == middle:
                return node
            node = node.next
            count += 1
