# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp =[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
s =Solution()
print(s.uniquePaths(3,7))