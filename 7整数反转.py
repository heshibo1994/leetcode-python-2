# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#  示例 2:
#
# 输入: -123
# 输出: -321
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            x = str(x)[::-1]
            return int(x)
        else:
            x = "-"+str(x)[1:][::-1]
            return int(x)
s=Solution()
print(s.reverse(-123333456))

