from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        graph = {}
        def dfs(node):
            if node is None:
                return
            if node.left:
                if node.val not in graph:
                    graph[node.val] = set()
                graph[node.val].add(node.left.val)
            if node.right:
                if node.val not in graph:
                    graph[node.val] = set()
                graph[node.val].add(node.right.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)

        m = 0
        for i in graph:
            q = deque([i])
            visit = set()
            while q:
                current = q.popleft()
                visit.add(current)
                if current in graph:
                    for j in graph[current]:
                        graph[i].add(j)
                        if j not in visit:
                            q.append(j)
        for i in graph:
            m = max(
                [
                    m,
                    abs(i - min(graph[i])),
                    abs(i - max(graph[i]))
                ]
                )

        return m
