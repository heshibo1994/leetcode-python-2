# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
class Solution:
    def reverseOnlyLetters(self, S):
        alpha = ""
        other = ""
        l = []
        ans = ""
        for i in S:
            if i.isalpha():
                alpha = i + alpha
            else:
                other = other +i
        k = 0
        for i in S:
            if i.isalpha():
                ans = ans+alpha[k]
                k = k+1
            else:
                ans =ans+i
        return ans
s=Solution()
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))