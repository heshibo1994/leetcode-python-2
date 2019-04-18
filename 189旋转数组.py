# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        class Solution:
            def rotate(self, nums, k):
                """
                :type nums: List[int]
                :type k: int
                :rtype: void Do not return anything, modify nums in-place instead.
                """
                nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))