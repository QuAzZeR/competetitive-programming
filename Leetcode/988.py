from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        answer = []

        def dfs(node, path):
            if node is None:
                return ""
            if node.left is None and node.right is None:
                path += chr(node.val + 97)
                path = path[::-1]
                answer.append(path)
                return
            dfs(node.left, path + chr(node.val + 97))
            dfs(node.right, path + chr(node.val + 97))

        dfs(root, "")
        answer.sort()
        return answer[0]
