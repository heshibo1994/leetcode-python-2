# 如果数组是单调递增或单调递减的，那么它是单调的。
#
# 如果对于所有
# i <= j，A[i] <= A[j]，那么数组
# A
# 是单调递增的。 如果对于所有
# i <= j，A[i] > = A[j]，那么数组
# A
# 是单调递减的。
#
# 当给定的数组
# A
# 是单调数组时返回
# true，否则返回
# false。
#
#
#
# 示例
# 1：
#
# 输入：[1, 2, 2, 3]
# 输出：true
#
# 示例
# 2：
#
# 输入：[6, 5, 4, 4]
# 输出：true
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if sorted(A) == A or sorted(A)[::-1] == A:
            return True
        return False



