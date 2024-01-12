from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.answer = None
        def dfs(node):
            if node is None:
                return
            if node.val == val:
                self.answer = node
            if self.answer is not  None:
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.answer
