# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
#
# 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。
#
# 例如 :
# 输入:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# 输出: 3
# 解释: 满足条件的子数组: [2], [2, 1], [3].
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        left = 0
        right = 1
        ans = []
        while right < len(A):
            if L <= max(A[left:right]) <= R:
                ans.append(A[left:right])

            else:
                left = right
                right +=1
        if L <= max(A[left:right]) <= R:
            ans.append(A[left:right])
        return ans

s = Solution()
print(s.numSubarrayBoundedMax([2,9,2,5,6],2,8))