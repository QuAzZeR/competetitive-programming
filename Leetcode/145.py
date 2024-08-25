from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            self.answer.append(node.val)
        dfs(root)
        return self.answer
