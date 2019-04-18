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
        dp[0][0] = matrix[0][0]
        dp[0][1] = matrix[0][1]
        dp[1][0] = matrix[1][0]
        l = 0
        for i in range(1,l1):
            for j in range(1,l2):
                if matrix[i][j] ==1:
                    dp[i][j] = dp[i-1][j-1]+l-1
                    l =l+1



s = Solution()
print(s.maximalSquare([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1, ], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))
