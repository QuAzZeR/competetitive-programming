# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.answer = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.travelling(cloned, target)
        return self.answer

    def travelling(self, current: TreeNode, target: TreeNode):
        if current is None:
            return
        if current.val == target.val:
            self.answer = current
            return
        self.travelling(current.left, target)
        self.travelling(current.right, target)

