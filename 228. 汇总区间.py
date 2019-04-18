# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
# 示例 1:
#
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#
# 示例 2:
#
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#
class Solution:
    def summaryRanges(self, nums):
        ans = []
        temp = [nums[0]]
        for i in range(0,len(nums)-1):
            if nums[i+1] - nums[i] ==1:
                temp.append(nums[i+1])
            else:
                ans.append(temp)
                temp = [nums[i+1]]
        if nums[-1]-nums[-2]==1:
            ans.append(temp)
        else:
            ans.append([temp[-1]])
        res = []
        for i in range(len(ans)):
            if len(ans[i])==1:
                res.append(str(ans[i][0]))
            else:
                res.append(str(ans[i][0])+"->"+str(ans[i][-1]))
        return res
s=Solution()
print(s.summaryRanges([0,2,3,4,6,8,9,11]))

