# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
    ###dfs
        # ans = []
        # def dfs(alpha,start,l):
        #     if "".join(l)==s:
        #         ans.append(l[:])
        #         return
        #     for i in range(start,len(s)):
        #         alpha = alpha +s[i]
        #         print("alpha",alpha)
        #         if 0<int(alpha)<=26:
        #             l.append(alpha)
        #             print(l)
        #             dfs("",i+1,l)
        #             l.pop()
        #         else:
        #             return
        #
        # dfs("",0,[])
        # return ans
    ### dp
        dp = [1]+[0]*len(s)
        for i in range(1,len(s)+1):
            if s[i-1] !="0":
                dp[i] = dp[i-1]
            if "09"<s[i-2:i]<"27":
                dp[i] =dp[i]+dp[i-2]
        return dp[-1]
s=Solution()
print(s.numDecodings("22434"))