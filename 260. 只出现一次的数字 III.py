# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        bit = 1
        for i in nums:
            temp = temp ^ i

        n = len(str(bin(temp)))-3  # 最高位为1
        a,b=0,0
        for i in nums:
            if i>>n&1:
                a^=i
            else:
                b^=i
        return b,a
s=Solution()
print(s.singleNumber([1,2,1,3,2,5]))

print(5^4)

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 0
        if N==1:
            return 1
        F = [0]*N
        F[0] = 0
        F[1] = 1
        for i in range(2,N):
            F[i] = F[i-1] +F[i-2]
        return F[-1]