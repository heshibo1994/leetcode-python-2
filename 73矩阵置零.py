# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = 0
        n = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        # for i in range(len(matrix)):
        #     if matrix[i][0] ==0:
        #         for j in range(len(matrix[0])):
        #             matrix[i][j] = 0




        return matrix
s=Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,0]]))