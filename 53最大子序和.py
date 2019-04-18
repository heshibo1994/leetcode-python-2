# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0  # 和
        sum = 0  # 最大和
        for i in range(len(nums)):
            if s <0:
                s = 0
            s = s+nums[i]
            sum = max(sum,s)
        return sum
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

