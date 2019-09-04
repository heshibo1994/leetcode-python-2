# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
#     如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
#     使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
#
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false
class Solution:
    def increasingTriplet(self, nums):
        min_num, mid_num = 0xffffffff, 0xffffffff  # 最小值，次小值
        for i in range(len(nums)):
            if nums[i] <= min_num:
                min_num = nums[i]
            elif nums[i] <= mid_num:
                mid_num = nums[i]
            else:
                return True
        return False
s = Solution()
print(s.increasingTriplet([1,1,1]))

