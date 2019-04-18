# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 20 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 24 = 16
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = n//2
        j = n % 2
        while not j:
            if i ==1:
                return True
            i,j = i//2,i%2
        return False
s = Solution()
for i in range(1,100):
    print(i,s.isPowerOfTwo(i))


