# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1,n+1))
        ans = []
        def dfs(start,l):
            if len(l)==k:
                ans.append(l[:])
                return
            for i in range(start,n):
                l.append(nums[i])
                dfs(i+1,l)
                l.pop()
        dfs(0,[])
        return ans

s=Solution()
print(s.combine(4,2))