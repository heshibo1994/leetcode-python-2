# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        length = len(nums)
        def dfs(l):
            if len(l) == length:
                ans.append(l[:])
                return
            for i in range(len(nums)):
                if nums[i] not in l:
                    l.append(nums[i])
                    dfs(l)
                    l.remove(nums[i])

        dfs([])
        return ans
s=Solution()
print(s.permute([1,2,3]))


