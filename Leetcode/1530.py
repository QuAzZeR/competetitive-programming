import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.answer = 0

        def dfs(node):
            m = [0] * 11
            if node is None:
                return m
            if node.left is None and node.right is None:
                m[1] = 1

            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(1, distance):
                for j in range(1, distance + 1 - i):
                    self.answer += left[i] * right[j]
            for i in range(2, 11):
                m[i] += left[i - 1] + right[i - 1]
            return m

        dfs(root)
        return self.answer
