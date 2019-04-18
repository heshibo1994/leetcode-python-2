# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        ans.append([1])
        for i in range(1, rowIndex+1):
            temp = [1]
            for j in range(i-1):
                temp.append(ans[i-1][j]+ans[i-1][j+1])
            temp.append(1)
            ans.append(temp)
            temp = []
        return ans[-1]