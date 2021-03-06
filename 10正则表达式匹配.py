# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
#
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
#     s 可能为空，且只包含从 a-z 的小写字母。
#     p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        v = re.match(p,s)
        return True if v==s else False
