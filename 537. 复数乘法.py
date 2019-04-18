# 给定两个表示复数的字符串。
#
# 返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。
#
# 示例 1:
#
# 输入: "1+1i", "1+1i"
# 输出: "0+2i"
# 解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
#
# 示例 2:
#
# 输入: "1+-1i", "1+-1i"
# 输出: "0+-2i"
# 解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
class Solution:
    def complexNumberMultiply(self, a,b):
        a1,a2 = int(a.split("+")[0]),int(a.split("+")[1][:-1])
        b1, b2 = int(b.split("+")[0]), int(b.split("+")[1][:-1])
        ans =  str(a1*b1-a2*b2)+"+"+str(a1*b2+b1*a2)+"i"
        print(ans)
s=Solution()
s.complexNumberMultiply( "1+1i", "1+1i")