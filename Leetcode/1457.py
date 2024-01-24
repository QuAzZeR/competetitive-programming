from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, bit):
        if node is None:
            return 0
        bit ^= 1 << node.val
        if node.left is None and node.right is None:
            return int((bit & (bit - 1)) == 0)
        return self.dfs(node.left, bit) + self.dfs(node.right, bit)


