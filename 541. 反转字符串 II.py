# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
# 如果剩余少于 k 个字符，则将剩余的所有全部反转。
# 如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
#
# 示例:
#
# 输入: s = "abcdefgh", k = 2
# 输出: "bacdfeg"
#
# 要求:
#
#     该字符串只包含小写的英文字母。
#     给定字符串的长度和 k 在[1, 10000]范围内。
#
# #
class Solution:
    def reverseStr(self, s,k):
        n = len(s) // (2 * k)
        temp = [s[i*2*k:2*k+i*2*k] for i in range(n+1)]
        ans = ""
        print(temp)
        if len(temp)!=0:
            for i in range(n):
                ans = ans+temp[i][:k][::-1]+temp[i][k:]
            if len(temp[-1])<k:
                ans = ans+temp[-1][::-1]
            elif k<=len(temp[-1])<2*k:
                ans = ans+temp[-1][:k][::-1]+temp[-1][k:]
        else:
            if len(s)<k:
                ans = ans+s[::-1]
            elif k<=len(s)<2*k:
                ans = ans+s[:k][::-1]+s[k:]
        return ans
s =Solution()
print(s.reverseStr("abcdefg",1))

