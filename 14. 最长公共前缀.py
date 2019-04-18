# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans =""
        flag  = True
        k = min(len(i) for i in strs)
        for i in range(k):
            for j in range(1,len(strs)):
                if strs[0][i] !=strs[j][i]:
                    flag = False
                    break
            if not flag:
                break
            else:
                ans +=strs[0][i]
        return ans
s=Solution()
print(s.longestCommonPrefix(["c","c"]))


