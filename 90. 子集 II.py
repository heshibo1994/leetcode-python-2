# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        def dfs(k,l):
            if l in ans:
                return
            ans.append(l[:])
            for i in range(k,len(nums)):
                l.append(nums[i])
                dfs(i+1,l)
                l.pop()
        dfs(0,[])
        return ans
s = Solution()
print(s.subsetsWithDup([1,2,3]))