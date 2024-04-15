from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def dfs(node, current):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.answer += int(current + str(node.val))
                print(self.answer, current)
                return
            dfs(node.left, current + str(node.val))
            dfs(node.right, current + str(node.val))

        dfs(root, "")
        return self.answer
