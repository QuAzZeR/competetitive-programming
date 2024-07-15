from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        s = set()
        m = {}

        def build_tree(v):
            n = TreeNode(v)
            if v in m:
                if m[v][0] is not None:
                    n.left = build_tree(m[v][0])
                if m[v][1] is not None:
                    n.right = build_tree(m[v][1])
            return n

        for p, c, l in descriptions:
            if p not in m:
                m[p] = [None, None]
            s.add(c)
            m[p][int(not l)] = c
        h = 0
        for p in m:
            if p not in s:
                h = p
                break
        h = build_tree(h)
        return h
