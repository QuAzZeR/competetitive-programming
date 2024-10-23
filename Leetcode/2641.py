from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a):
            if not a:
                return
            s = 0
            for node in a:
                if node is None:
                    continue
                if node.left:
                    s += node.left.val
                if node.right:
                    s += node.right.val
            aa = []
            for node in a:
                c = 0
                if node.left:
                    c += node.left.val
                if node.right:
                    c += node.right.val
                if node.left:
                    node.left.val = s - c
                    aa.append(node.left)
                if node.right:
                    node.right.val = s - c
                    aa.append(node.right)
            dfs(aa)

        root.val = 0
        dfs([root])
        return root
