# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans =""
        l = s.split()
        for i in range(len(l)):
            ans = ans+l[i][::-1]+" "
        return ans[:-1]
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
l = "fdsfds"
print(l[::-1])