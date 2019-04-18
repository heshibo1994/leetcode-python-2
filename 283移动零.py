# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[count]=nums[i]
                count +=1
        for j in range(count,len(nums)):
            nums[j] = 0


s =Solution()
s.moveZeroes([0,1,0,3,12])