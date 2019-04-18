# 给定一个方形整数数组
# A，我们想要得到通过
# A
# 的下降路径的最小和。
#
# 下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
#
#
#
# 示例：
#
# 输入：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：12
# 解释：
# 可能的下降路径有：
#
# [1, 4, 7], [1, 4, 8], [1, 5, 7], [1, 5, 8], [1, 5, 9]
# [2, 4, 7], [2, 4, 8], [2, 5, 7], [2, 5, 8], [2, 5, 9], [2, 6, 8], [2, 6, 9]
# [3, 5, 7], [3, 5, 8], [3, 5, 9], [3, 6, 8], [3, 6, 9]
#
# 和最小的下降路径是[1, 4, 7]，所以答案是
# 12。
class Solution:
    def minFallingPathSum(self, A):
        dp = []
        dp.append(A[0])
        row = len(A[0])-1
        for i in range(1,len(A)):
            temp = []
            temp.append(min(dp[i-1][0],dp[i-1][1])+A[i][0])
            for j in range(1,len(A[0])-1):
                temp.append(min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+A[i][j])
            temp.append(min(dp[i-1][row],dp[i-1][row-1])+A[i][row])
            dp.append(temp)
        return min(dp[-1])
s = Solution()
print(s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))