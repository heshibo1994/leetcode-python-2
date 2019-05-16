# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
class Solution:
    def reverseVowels(self, s):
        alpha = ""
        other = ""
        l = []
        ans = ""
        for i in s:
            if i in "aeiouAEIOU":
                alpha = i + alpha
            else:
                other = other +i
        k = 0
        for i in s:
            if i in "aeiouAEIOU":
                ans = ans+alpha[k]
                k = k+1
            else:
                ans =ans+i
        return ans
