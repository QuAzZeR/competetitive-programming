from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.s = [0] * 10**5
        def dfs(node, l):
            if node is None:
                return
            self.s[l] += node.val
            dfs(node.left, l+1)
            dfs(node.right, l+1)
        dfs(root, 0)
        self.s.sort(reverse=True)
        if self.s[k-1] == 0:
            return -1
        return self.s[k-1]
