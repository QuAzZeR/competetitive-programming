# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.answer = 0

        def dfs(node, parents):
            if node is None:
                return
            if len(parents) >= 2:
                if parents[-2] % 2 == 0:
                    self.answer += node.val

            dfs(node.left, parents + [node.val])
            dfs(node.right, parents + [node.val])

        dfs(root, [])
        return self.answer
