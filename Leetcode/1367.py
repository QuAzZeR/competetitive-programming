from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        n = len(values)
        def travel(node, i, j):
            if i == n:
                return True
            if node is None:
                return False
            if values[i] == node.val:
                i += 1
            elif values[j] == node.val:
                j += 1
            else:
                i = j
            return travel(node.left, i, j) or travel(node.right, i, j)

        return travel(root, 0, 0)
