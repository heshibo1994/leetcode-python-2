# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.func(res,"",0,0,n)
        return res

    def func(self,res,s,l,r,n):
        if (l>n or r>n or r>l):
            return
        if (l==n and r==n):
            res.append(s)
            return
        self.func(res,s+'(',l+1,r,n)
        self.func(res,s+')',l,r+1,n)

s = Solution()
print(s.generateParenthesis(3))
