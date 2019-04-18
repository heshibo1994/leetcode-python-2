"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        child_depth = 0
        for child in root.children:
            child_depth = max(child_depth, self.maxDepth(child))
        return child_depth + 1
