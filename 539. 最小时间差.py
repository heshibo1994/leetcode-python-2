# 给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示
# 示例 1：
#
# 输入: ["23:59","00:00"]
# 输出: 1
class Solution:
    def findMinDifference(self, timePoints):
        timePoints = [int(t.split(":")[0])*60+int(t.split(":")[1]) for t in timePoints]
        timePoints = timePoints +[i+24*60 for i in timePoints]
        timePoints.sort()
        ans = (timePoints[1]-timePoints[0])
        for i in range(1,len(timePoints)):
            ans = min(ans,timePoints[i]-timePoints[i-1])
        return ans

s =Solution()
print(s.findMinDifference(["05:31","22:08","00:35"]))