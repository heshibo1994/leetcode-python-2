# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
class Solution:
    def search(self, nums, target):
        # if nums[0] == target:
        #     return 0
        # if nums[-1] ==target:
        #     return len(nums)-1
        start = 0
        end = len(nums)-1
        while(start<=end):
            if nums[0] == target:
                return 0
            if nums[-1] ==target:
                return len(nums)-1


            mid = (start+end)//2
            if nums[mid]<target:
                start = mid
            elif nums[mid]>target:
                end = mid
            else:
                return (start+end)//2
        return -1
s=Solution()
print(s.search([-1,0,3,5,9,12],2))
