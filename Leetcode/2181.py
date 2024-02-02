from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        current = None
        s = 0
        is_started = False
        while head is not None:
            if head.val == 0:
                if not is_started:
                    is_started = True
                else:
                    if current is None:
                        new_head = ListNode(s)
                        current = new_head
                    else:
                        temp = ListNode(s)
                        current.next = temp
                        current = temp
                    s = 0
            else:
                s += head.val
            head = head.next
        return new_head
