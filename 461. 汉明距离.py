# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
class Solution:
    def hammingDistance(self, x, y):
        x = "0"*(34-len(bin(x)))+bin(x)[2:]
        y = "0" * (34 - len(bin(y))) + bin(y)[2:]
        ans = 0
        for i in range(32):
            if x[i]!=y[i]:
                ans =ans+1
        return ans
s = Solution()
print(s.hammingDistance(1,4))

