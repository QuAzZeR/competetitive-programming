from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.answer = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            self.answer.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.answer
