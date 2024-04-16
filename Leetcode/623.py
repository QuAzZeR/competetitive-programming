from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        def dfs(node, d):
            if node is None:
                return 0
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
            if d + 1 == depth:
                cur = TreeNode(val, left=node.left)
                node.left = cur
                cur = TreeNode(val, right=node.right)
                node.right = cur

        if depth == 1:
            if root is not None:
                cur = TreeNode(val, left=root)
                return cur
            else:
                root = TreeNode(val)
            return root
        dfs(root, 1)
        return root
