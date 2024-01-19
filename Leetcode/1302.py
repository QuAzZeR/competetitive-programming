from collections import defaultdict
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.s = defaultdict(int)
        self.m = 0
        self.travel(root, 0)
        return self.s[self.m]

    def travel(self, node, level):
        if node is None:
            if self.m < level-1:
                self.m = level-1
            return

        self.s[level] += node.val
        self.travel(node.left, level + 1)
        self.travel(node.right, level + 1)


