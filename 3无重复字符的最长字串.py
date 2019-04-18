# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {}
        ans = 0
        j = 0
        for i in range(len(s)):
            if s[i] in a:
                ans = max(i-j, ans)
                nums = i
                m = max(m,a[s[i]]+1)
            a[s[i]] = i
        return max(ans,len(s)-m)

s =Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))