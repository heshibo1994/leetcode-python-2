# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2,int(n**0.5)+1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0] * len(prime[i*i:n:i])
                print(i,prime)
        return sum(prime)
s = Solution()
print(s.countPrimes(100))



