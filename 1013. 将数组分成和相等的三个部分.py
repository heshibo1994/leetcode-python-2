# 给定一个整数数组
# A，只有我们可以将其划分为三个和相等的非空部分时才返回
# true，否则返回
# false。
#
# 形式上，如果我们可以找出索引
# i + 1 < j
# 且满足(A[0] + A[1] + ... + A[i] == A[i + 1] + A[i + 2] + ... + A[j - 1] == A[j] + A[j - 1] + ... + A[A.length - 1])
# 就可以将数组三等分。
#
#
#
# 示例
# 1：
#
# 输出：[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
class Solution:
    def canThreePartsEqualSum(self, A):
        if sum(A)%3!=0:
            return False
        else:
            a = sum(A)//3
        temp =0
        times=0
        for i in range(len(A)):
            temp = temp +A[i]
            if temp==a:
                temp = 0
                times=times+1
        return True if times==3 and temp==0 else False
s =Solution()
print(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))