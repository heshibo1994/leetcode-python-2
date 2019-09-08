# 题目描述
# 评论(47)
# 题解(33)
# New
# 提交记录
#
# 给你一个长度固定的整数数组
# arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
#
# 注意：请不要在超过该数组长度的位置写入元素。
#
# 要求：请对输入的数组
# 就地
# 进行上述修改，不要从函数返回任何东西。
#
#
#
# 示例
# 1：
#
# 输入：[1, 0, 2, 3, 0, 4, 5, 0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1, 0, 0, 2, 3, 0, 0, 4]
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        s = 0
        k_zero = 0
        while s<len(arr) :
            if arr[s] == 0 :
                arr.insert(s,0)
                arr.pop()
                s +=2
            else:
                s +=1
        print(arr)

s = Solution()
s.duplicateZeros([1,0,2,3,0,4,5,0])
