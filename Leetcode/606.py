from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.answer = str(root.val)
        self.travel(root.left)
        self.travel(root.right)
        return self.answer

    def travel(self, node):
        if node is None:
            self.answer += '()'
            return

        self.answer += '(' + str(root.val)
        self.travel(root.left)
        self.travel(root.right)
        answer += ')'
