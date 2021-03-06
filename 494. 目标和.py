# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
# 示例 1:
#
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。
class Solution:
    def findTargetSumWays(self, nums, S):
        target = (sum(nums)+S)//2
        ans = []

        def dfs(l,start):
            if len(l)!=0 and sum(l) == target:
                ans.append(l[:])
                return
            for i in range(start,len(nums)):
                l.append(nums[i])
                dfs(l,i+1)
                l.pop()
        dfs([],0)
        return ans
s = Solution()
print(s.findTargetSumWays([1,2,3,4,4,5],3))



