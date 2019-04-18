# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def dfs(ip, start,l):
            if len(l) == 4:
                if isip(l[-1]):
                    ans.append(l[:])
                    return
                return
            for i in range(start,len(s)):
                if len(l)==3:
                    ip = ip + s[i:]
                else:
                    ip = ip +s[i]
                if isip(ip):
                    l.append(ip)
                    dfs("",i+1,l)
                    l.pop()
                else:
                    return


        def isip(n):
            if n.startswith("0") and len(n)!=1:
                return False
            n = int(n)
            return True if  0<=n<=255 else False
        def ip(l):
            res = []
            for i in range(len(l)):
                if sum(map(len, l[i])) == len(s):
                    res.append(".".join(l[i]))
            return res
        dfs("",0 ,[])
        return ip(ans)
s = Solution()

print(s.restoreIpAddresses("101023"))
print(s.restoreIpAddresses("25525511135"))