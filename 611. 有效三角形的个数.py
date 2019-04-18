# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
#
# 示例 1:
#
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for i in range(len(nums)-1,1,-1):
            start = 0
            end = i-1
            while start<end:
                if nums[start]+nums[end]>nums[i]:
                    ans =ans+end-start
                    end = end-1
                else:
                    start = start +1
        return ans
s=Solution()
print(s.triangleNumber([2,2,3,4]))
l = [1,233,4]
print([1,233,4]==l)