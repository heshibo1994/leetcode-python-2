# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
# 暴力法
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]f
        :type target: int
        :rtype: List[int]
        """
#         l = len(nums)
#         for i in range(l):
#             for j in range(i+1, l):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]
        a = {}
        for i in range(len(nums)):
            if target-nums[i] in a:
                return [a[target-nums[i]],i]
            if nums[i] not in a:
                a[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
s =Solution()
print(s.twoSum(nums,target))