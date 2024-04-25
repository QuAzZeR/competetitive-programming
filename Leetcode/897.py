# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        s = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            s.append(node.val)
            dfs(node.right)

        def right(s):
            if s:
                return TreeNode(s[0], right=right(s[1:]))

        dfs(root)
        return right(s)
