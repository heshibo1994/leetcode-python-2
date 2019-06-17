# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
#
# 输入: 100
# 输出: "202"
#
# 示例 2:
#
# 输入: -7
# 输出: "-10"
#
# 注意: 输入范围是 [-1e7, 1e7] 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/base-7
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans = ""
        flag = ""
        if num<0:
            flag = "-"
            num = -num
        while (num):
            ans = str(num%7)+ans
            num = int(num/7)
        return flag+ans
s=Solution()
print(s.convertToBase7(101))


