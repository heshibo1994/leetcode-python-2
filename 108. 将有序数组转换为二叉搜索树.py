# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return
        mid = len(nums)//2
        pNode = TreeNode(nums[mid])
        pNode.left = self.sortedArrayToBST(nums[:mid])
        pNode.right = self.sortedArrayToBST(nums[mid+1:])
        return pNode
