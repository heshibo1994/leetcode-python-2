# 给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
#
# 示例:
#
# nums = [1, 2, 3]
# target = 4
#
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# class Solution:
#     def combinationSum4(self, nums,target):
#         ans = []
#         def dfs(l):
#             if sum(l) == target:
#                 ans.append(l[:])
#                 print(l[:])
#                 return
#             elif sum(l) > target:
#                 return
#             else:
#                 for i in range(len(nums)):
#                     l.append(nums[i])
#                     dfs(l)
#                     l.pop()
#         dfs([])
#         return ans
# s =Solution()
# print(s.combinationSum4([4,2,1],32))
class Solution:
    def combinationSum4(self, nums,target):
        dp = [1]+[0]*target
        for i in range(1,target+1):
            for j in nums:
                if i>=j:
                    dp[i] =dp[i-j]+dp[i]
        return dp[-1]
s =Solution()
print(s.combinationSum4([4,2,1],32))