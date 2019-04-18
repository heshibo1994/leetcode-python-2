# 给定一个 N 叉树，返回其节点值的前序遍历。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root):
        if root is None:
            return []
        result=[root.val]
        for child in root.children:
            a = self.preorder(child)
            result = result+a
        return result

