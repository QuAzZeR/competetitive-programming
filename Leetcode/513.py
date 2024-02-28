from typing import Optional
from collections import Queue, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.layer = defaultdict(list)
        self.m = 0

        def dfs(node, level):
            if node is None:
                if self.m < level:
                    self.m = level
                return
            self.layer[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return self.layer[self.m - 1][0]
