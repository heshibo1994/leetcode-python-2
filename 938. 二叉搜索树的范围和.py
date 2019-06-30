# 给定二叉搜索树的根结点
# root，返回
# L
# 和
# R（含）之间的所有结点的值的和。
#
# 二叉搜索树保证具有唯一的值。
#
#
#
# 示例
# 1：
#
# 输入：root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
# 输出：32
#
# 示例
# 2：
#
# 输入：root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], L = 6, R = 10
# 输出：23
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / range - sum - of - bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root,L,R):
        ans = []
        if root is None:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right,L,R)
        if root.val > R:
            return self.rangeSumBST(root.left,L,R)
        else:
            return root.val + self.rangeSumBST(root.right,L,R)+self.rangeSumBST(root.left,L,R)


