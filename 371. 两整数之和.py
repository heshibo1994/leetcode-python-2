# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#
# 示例 1:
#
# 输入: a = 1, b = 2
# 输出: 3
#
# 示例 2:
#
# 输入: a = -2, b = 3
# 输出: 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-two-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def getSum(self, a, b):
        carry = a & b
        sum = a^b
        while(carry != 0 ):
            b = carry<<1
            carry = sum & (b)
            sum^=b
        return sum
s = Solution()
print(s.getSum(2,4))

print(bin(-3))


