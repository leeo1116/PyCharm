__author__ = 'liangl2'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_h = self.depth(root.left)
        right_h = self.depth(root.right)
        return abs(left_h-right_h) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1

    # https://leetcode.com/discuss/22898/the-bottom-up-o-n-solution-would-be-better