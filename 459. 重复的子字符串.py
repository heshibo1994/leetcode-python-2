# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
#
# 示例 1:
#
# 输入: "abab"
#
# 输出: True
#
# 解释: 可由子字符串 "ab" 重复两次构成。
#
# 示例 2:
#
# 输入: "aba"
#
# 输出: False
class Solution:
    def repeatedSubstringPattern(self, s):
        l = len(s)
        temp = [1]
        for i in range(2,l):
            if l%i==0:
                temp.append(i)
        for i in temp:
            if s[:i]*(l//i)==s:
                return True
        return False
s = Solution()
print(s.repeatedSubstringPattern("abcabc"))

