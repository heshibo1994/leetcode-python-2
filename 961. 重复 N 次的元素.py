# 在大小为
# 2
# N
# 的数组
# A
# 中有
# N + 1
# 个不同的元素，其中有一个元素重复了
# N
# 次。
#
# 返回重复了
# N
# 次的那个元素。
#
#
#
# 示例
# 1：
#
# 输入：[1, 2, 3, 3]
# 输出：3
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = []
        for i in A:
            if i not in a:
                a.append(i)
            else:
                return i
