from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(current):
            if current == None:
                return
            if current.val >= low and current.val <= high:
                self.sum += current.val
            dfs(current.left)
            dfs(current.right)
        dfs(root)
        return self.sum
