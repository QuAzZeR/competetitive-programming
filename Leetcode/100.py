from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.answer = True
        self.travel(p, q)
        return self.answer

    def travel(self, node1, node2):
        if not self.answer:
            return
        if node1 is None and node2 is None:
            return
        if node1 is None and node2 is not None:
            self.answer = False
            return
        if node1 is not None and node2 is None:
            self.answer = False
            return
        if node1.val != node2.val:
            self.answer = False
            return
        self.travel(node1.left, node2.left)
        self.travel(node1.right, node2.right)
