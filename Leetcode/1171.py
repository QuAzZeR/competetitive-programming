from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum_node = {}
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sum_node:
                prev = prefix_sum_node[prefix_sum]
                to_delete = prev.next
                p = prefix_sum + (to_delete.val if to_delete else 0)
                while p != prefix_sum:
                    del prefix_sum_node[p]
                    to_delete = to_delete.next
                    p += to_delete.val if to_delete else 0
                prev.next = current.next
            else:
                prefix_sum_node[prefix_sum] = current
            current = current.next
        return dummy.next
