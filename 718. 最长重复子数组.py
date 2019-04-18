# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
#
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l1 = len(A)
        l2 = len(B)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(max(row) for row in dp)
s = Solution()
print(s.findLength([1,2,3,2,1],[3,2,1,4,7]))