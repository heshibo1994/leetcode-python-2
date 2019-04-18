# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        t = 100000
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) <= t:
                    t = abs(s - target)
                    ans =s
                if s < target:
                    l = l + 1
                elif s > target:
                    r = r - 1
                else:
                    return s
        return ans
s = Solution()
print(s.threeSumClosest([-1, 1, 2, -4], 1))
print(s.threeSumClosest([1,1,1,0],-100))
