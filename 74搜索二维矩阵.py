# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#     每行中的整数从左到右按升序排列。
#     每行的第一个整数大于前一行的最后一个整数。
#
# 示例 1:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
# 示例 2:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums = [i for item in matrix for i in item]
        l = 0
        r = len(nums)-1
        while(l<=r):
            m = (l+r)//2
            if nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1
            else:
                return True
        return False


s=Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))