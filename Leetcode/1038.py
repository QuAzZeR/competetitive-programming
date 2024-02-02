# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def dfs(node, val):
            if node.right:
                val = dfs(node.right, val)
            val += node.val
            node.val = val
            if node.left:
                val = dfs(node.left, val)
            return val

        dfs(root, 0)
        return root
