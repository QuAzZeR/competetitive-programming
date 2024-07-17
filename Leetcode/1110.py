from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        self.delete_set = set(to_delete)
        self.answer = []

        def dfs(node, flag):
            if not node:
                return None
            to_del = node.val in self.delete_set
            node.left = dfs(node.left, to_del)
            node.right = dfs(node.right, to_del)
            if not to_del and flag:
                self.answer.append(node)
            return None if to_del else node

        dfs(root, True)
        return self.answer
