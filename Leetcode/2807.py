from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = head
        current = previous.next
        while current is not None:
            c = current.val
            p = previous.val
            max_val = max(c,p)
            for i in range(max_val,0,-1):
                if c%i == 0 and p%i == 0:
                    new = ListNode(val=i, next=current)
                    previous.next = new
                    previous = current
                    current = current.next
                    break

        return head

