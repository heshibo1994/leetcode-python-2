# 对于一个
# 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
#
# 给定一个
# 正整数
# n， 如果他是完美数，返回
# True，否则返回
# False
#
# 示例：
#
# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / perfect - number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans =[]
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                ans.append(i)
                ans.append(num//i)
        return ans
        return True if sum(ans)==num-1 else False
s=Solution()
print(s.checkPerfectNumber(36))

