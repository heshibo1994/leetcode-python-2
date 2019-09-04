# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#
# 示例 2:
#
# 输入:
# s = "ababbc", k = 2
#
# 输出:
# 5
#
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
class Solution(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


s = Solution()
print(s.longestSubstring(s = "ababbc", k = 2))
