# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        l1 = len(matrix)
        l2 = len(matrix[0])
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        print(dp)
        ans = 0
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] ==1:
                    dp[i][j] =min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans = max(ans,dp[i][j])
        return ans**2








s = Solution()
print(s.maximalSquare([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1, ], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))
