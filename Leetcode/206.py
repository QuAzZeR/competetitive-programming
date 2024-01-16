from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head

        new_head = ListNode(head.val)
        previous = new_head
        head = head.next
        while head != None:

            new_head = ListNode(head.val, previous)

            previous = new_head

            head = head.next

        return new_head
