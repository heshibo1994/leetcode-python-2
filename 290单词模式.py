# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(s) != len(pattern):
            return False
        if len(set(s)) != len(set(pattern)):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            else:
                if d[pattern[i]] != s[i]:
                    return False

        return True
s = Solution()
print(s.wordPattern(pattern = "abba", str = "dog cat cat dog"))