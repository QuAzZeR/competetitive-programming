from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = {}
        def dfs(node):
            if node is None:
                return
            if node.left:
                if node.val not in g:
                    g[node.val] = []
                g[node.val].append(node.left.val)
                if node.left.val not in g:
                    g[node.left.val] = []
                g[node.left.val].append(node.val)
            if node.right:
                if node.val not in g:
                    g[node.val] = []
                g[node.val].append(node.right.val)
                if node.right.val not in g:
                    g[node.right.val] = []
                g[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        visit = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                visit.add(current)
                if current not in g:
                    continue

                for i in g[current]:
                    if i not in visit:
                        queue.append(i)
        return time
