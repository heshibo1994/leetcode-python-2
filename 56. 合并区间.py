# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        ans = []
        res = []
        for i in range(len(intervals)):
            ans = ans+list(range(intervals[i][0],intervals[i][1]+1))
        ans = list(set(ans))
        ans.sort()
        temp = ans[0]
        for i in range(len(ans)-1):
            if ans[i+1]-ans[i]!=1:
                res.append([temp,ans[i]]+1)
                temp = ans[i+1]
        if ans[-1]-ans[-2]==1:
            res.append([temp, ans[-1]])
        return res

s = Solution()
print(s.merge( [[1,4],[5,6]],))


