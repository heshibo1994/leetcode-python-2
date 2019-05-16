# 给定有效字符串 "abc"。
#
# 对于任何有效的字符串 V，我们可以将 V 分成两个部分 X 和 Y，使得 X + Y（X 与 Y 连接）等于 V。（X 或 Y 可以为空。）那么，X + "abc" + Y 也同样是有效的。
#
# 例如，如果 S = "abc"，则有效字符串的示例是："abc"，"aabcbc"，"abcabc"，"abcabcababcc"。无效字符串的示例是："abccba"，"ab"，"cababc"，"bac"。
#
# 如果给定字符串 S 有效，则返回 true；否则，返回 false。
class Solution:
    def isValid(self, S):
        l = len(S)
        i=0
        while l:
            try:
                i = S.index("abc")
            except:
                return False
            else:
                S = S[0:i] + S[i+3:]
                l = l-3
        return True




s  =Solution()
print(s.isValid("aabcba"))


