# 翻转一棵二叉树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

