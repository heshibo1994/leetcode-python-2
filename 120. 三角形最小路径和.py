# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
class Solution:
    def minimumTotal(self, l):
        n = len(l)
        dp = [[l[0][0]]]
        for i in range(1,n):
            temp = []
            temp.append(l[i][0]+dp[i-1][0])
            for j in range(1,i):
                temp.append(min(dp[i-1][j-1],dp[i-1][j])+l[i][j])
            temp.append(l[i][i]+dp[i-1][i-1])
            dp.append(temp)
        return min(dp[-1])
s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))