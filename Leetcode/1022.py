from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(node, value):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.answer += int(value + str(node.val), 2)
                return
            dfs(node.left, value + str(node.val))
            dfs(node.right, value + str(node.val))

        dfs(root, '')
        return self.answer
