# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
#
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
#     给定 n 的范围是 [1, 9]。
#     给定 k 的范围是[1,  n!]。
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        def dfs(l):
            if len(l) == n:
                ans.append(l[:])
                if len(ans) ==k:
                    t = "".join([str(item) for item in l])
                    return t
                return
            for i in range(1,n+1):
                if i not in l:
                    l.append(i)
                    dfs(l)
                    l.pop()
        return dfs([])
s=Solution()
print(s.getPermutation(3,2))