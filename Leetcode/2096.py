from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(node, val, path):
            if node.val == val:
                return True
            if node.left and dfs(node.left, val, path):
                path += "L"
            elif node.right and dfs(node.right, val, path):
                path += "R"
            return path

        found_start = []
        found_destination = []
        dfs(root, startValue, found_start)
        dfs(root, destValue, found_destination)
        while (
            len(found_start)
            and len(found_destination)
            and found_start[-1] == found_destination[-1]
        ):
            found_start.pop()
            found_destination.pop()

        return "".join("U" * len(found_start) + "".join(reversed(found_destination)))
