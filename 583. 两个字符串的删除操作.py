# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
#
# 示例 1:
#
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for c in range(len(word2)+1)] for r in range(len(word1)+1)]
        for i in range(len(word1)):
            dp[i][0] = i
        for j in range(len(word2)):
            dp[0][j] = j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =dp[i-1][j-1]
                dp[i][j] = min(dp[i][j],dp[i][j-1]+1,dp[i-1][j]+1)
        return dp[-1][-1]
s = Solution()
print(s.minDistance("sea","eat"))