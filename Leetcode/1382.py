# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a = []

        def order(node):
            if node is None:
                return
            order(node.left)
            a.append(node.val)
            order(node.right)

        def BST(l, r):
            if l > r:
                return
            m = (l + r) // 2
            left_node = BST(l, m - 1)
            right_node = BST(m + 1, r)
            return TreeNode(a[m], left_node, right_node)

        order(root)
        return BST(0, len(a) - 1)
