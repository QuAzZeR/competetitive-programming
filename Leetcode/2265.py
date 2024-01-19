# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, [])
        return self.count

    def dfs(self, node, sub_tree):
            if node is None:
                return []
            sub_tree += self.dfs(node.left, [])
            sub_tree += self.dfs(node.right, [])
            sub_tree.append(node.val)
            s = sum(sub_tree)
            a = s//len(sub_tree)
            if a == node.val:
                self.count += 1
            return sub_tree
