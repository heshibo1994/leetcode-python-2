# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
class Solution:
    def countSubstrings(self, s):
        l = len(s)
        dp = [[0]*n for n in range(1,l+1)]
        print(dp)
        ans = 0
        for i in range(l):
            for j in range(i,-1,-1):
                if s[i]==s[j] and (i<=j+1 or dp[i-1][j+1] ==1):
                    dp[i][j] =1
                    ans = ans+1
        return ans

s = Solution()
print(s.countSubstrings("aaa"))
