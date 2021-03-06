# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#
#     二叉树的根是数组中的最大元素。
#     左子树是通过数组中最大值左边部分构造出的最大二叉树。
#     右子树是通过数组中最大值右边部分构造出的最大二叉树。
#
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums)==0:
            return None
        temp = max(nums)
        root = TreeNode(temp)
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(temp)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(temp):])
        return root

