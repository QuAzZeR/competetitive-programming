from collections import defaultdict
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.avg = defaultdict(list)
        def dfs(node,level):
            if node == None:
                return
            self.avg[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        return list(map(lambda x: sum(self.avg[x])/len(self.avg[x]), self.avg))
