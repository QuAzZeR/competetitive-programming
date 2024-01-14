from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node == None:
                return
            left = dfs(node.right)

            right = dfs(node.left)
            new_node = TreeNode(node.val, left, right)
            return new_node

        return dfs(root)
