# 给定一个二进制字符串
# S（一个仅由若干
# '0'
# 和
# '1'
# 构成的字符串）和一个正整数
# N，如果对于从
# 1
# 到
# N
# 的每个整数
# X，其二进制表示都是
# S
# 的子串，就返回
# true，否则返回
# false。
#
#
#
# 示例
# 1：
#
# 输入：S = "0110", N = 3
# 输出：true
#
# 示例
# 2：
#
# 输入：S = "0110", N = 4
# 输出：false
class Solution:
    def queryString(self, S,N):
        for i in range(N):
            if bin(i)[2:] not in S:
                return False
        return True
s=Solution()
print(s.queryString(S = "0110", N = 4))