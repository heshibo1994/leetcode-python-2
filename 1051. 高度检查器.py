# 学校在拍年度纪念照时，一般要求学生按照
# 非递减
# 的高度顺序排列。
#
# 请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以
# 非递减
# 高度排列的必要移动人数。
#
#
#
# 示例：
#
# 输入：[1, 1, 4, 2, 1, 3]
# 输出：3
# 解释：
# 高度为
# 4、3
# 和最后一个
# 1
# 的学生，没有站在正确的位置。
class Solution:
    def heightChecker(self, heights):
        ans = 0
        h = sorted(heights)
        for i in range(len(heights)):
            if h[i]!=heights[i]:
                ans+=1
        return ans