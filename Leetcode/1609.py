from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.d = defaultdict(list)

        def dfs(node, level):
            if node is None:
                return
            self.d[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        for i in self.d:
            l = self.d[i]
            for j in range(0, len(l)):
                if i % 2 == 0:
                    if j == 0:
                        if l[j] % 2 == 0:
                            return False
                    else:
                        if l[j] % 2 == 0:
                            return False
                        if l[j] <= l[j - 1]:
                            return False
                else:
                    if j == 0:
                        if l[j] % 2 != 0:
                            return False
                    else:
                        if l[j] % 2 != 0:
                            return False
                        if l[j] >= l[j - 1]:
                            return False
        return True
