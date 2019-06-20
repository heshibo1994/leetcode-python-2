# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
# #
class Solution:
    def maxProduct(self, nums):
        temp = []
        ans =[]
        for i in nums:
            if i!=0:
                temp.append(i)
            else:
                ans.append(temp)
                temp =[]

s=Solution()
print(s.maxProduct([2,3,0,-2,4]))
