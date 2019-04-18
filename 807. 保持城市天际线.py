# 例子：
# 输入： grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# 输出： 35
# 解释：
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# 从数组竖直方向（即顶部，底部）看“天际线”是：[9, 4, 8, 7]
# 从水平水平方向（即左侧，右侧）看“天际线”是：[8, 7, 9, 3]
#
# 在不影响天际线的情况下对建筑物进行增高后，新数组如下：
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        row = len(grid)
        col = len(grid[0])
        ans = []
        temp1 = []
        temp2 = []
        s = 0
        for i in range(row):
            temp1.append(max(grid[i]))
            s = s+sum(grid[i])
        for j in range(col):
            temp = []
            for i in range(row):
                temp.append(grid[i][j])
            temp2.append(max(temp))
        for i in range(row):
            for j in range(col):
                ans.append(min(temp1[i],temp2[j]))
        return sum(ans)-s
        print(ans)
        print(temp1)
        print(temp2)
s = Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))



