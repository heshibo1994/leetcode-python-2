# 给定一个 N 叉树，返回其节点值的后序遍历。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root):
        if root is None:
            return []

        result = [root.val]
        for child in root.children:
                reslut= self.preorder(child)+result
        return result