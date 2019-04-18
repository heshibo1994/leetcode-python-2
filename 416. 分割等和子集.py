# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
# 每个数组中的元素不会超过
# 100
# 数组的大小不会超过
# 200
#
# 示例
# 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成[1, 5, 5]
# 和[11].
#
# 示例
# 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total%2 ==1:
            return False
        else:
            target = total//2
        nums.sort()
        def dfs(start,target):
            if target == 0:
                return True
            if nums[start]>target :
                return False
            for i in range(start,len(nums)):
                if nums[i]<=target and i<len(nums):
                    if dfs(i+1,target-nums[i]):
                        return True
                else:
                    return False
        return dfs(0,target)

s = Solution()
print(s.canPartition([2,2,3,5]))