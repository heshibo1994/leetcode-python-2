# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1:
#
# 输入: [5,7]
# 输出: 4
#
# 示例 2:
#
# 输入: [0,1]
# 输出: 0
#
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = 0
        while(m!=n):
            m>>=1
            n>>=1
            k +=1
        return n<<k
print(5&6)
s=Solution()
print(s.rangeBitwiseAnd(5,7))

print(0&2147483647)