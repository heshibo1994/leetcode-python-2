# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans =[]
        length = len(s)
        def dfs(start,l):
            temp = ""
            if len("".join(l)) == length:
                ans.append(l[:])
                return
            for i in range(start,length):
                temp = temp + s[i]
                if temp[::-1] == temp:
                    l.append(temp)
                    dfs(i+1,l)
                    l.pop()
        dfs(0,[])
        return ans

s =Solution()
print(s.partition("aab"))
