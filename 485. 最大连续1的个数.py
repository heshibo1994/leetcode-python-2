# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        temp = 0
        for i in nums:
            if i==1:
                temp = temp+1
                ans = max(temp,ans)
            else:
                temp = 0
        return ans
s=Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

