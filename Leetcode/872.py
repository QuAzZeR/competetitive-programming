from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        left_node1 = []
        left_node2 = []
        def travel(node,left_node):
            if node is None:
                return

            if node.left is None and node.right == None:
                left_node.append(node.val)
                return

            travel(node.left,left_node)
            travel(node.right,left_node)
            return False
        travel(root1,left_node1)
        travel(root2,left_node2)
        return left_node1 == left_node2

