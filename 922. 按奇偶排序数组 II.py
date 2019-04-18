# 给定一个非负整数数组
# A， A
# 中一半整数是奇数，一半整数是偶数。
#
# 对数组进行排序，以便当
# A[i]
# 为奇数时，i
# 也是奇数；当
# A[i]
# 为偶数时， i
# 也是偶数。
#
# 你可以返回任何满足上述条件的数组作为答案。
#
#
#
# 示例：
#
# 输入：[4, 2, 5, 7]
# 输出：[4, 5, 2, 7]
# 解释：[4, 7, 2, 5]，[2, 5, 4, 7]，[2, 7, 4, 5]
# 也会被接受。
class Solution:
    def sortArrayByParityII(self, A):
        ans = []
        l1 = [i for i in A if i%2 ==0 ]
        l2 = [i for i in A if i%2 ==1 ]
        for i in range(len(l1)):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans
s=Solution()
print(s.sortArrayByParityII([4,2,5,7]))

