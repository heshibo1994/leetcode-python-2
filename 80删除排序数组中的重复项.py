# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定 nums = [1,1,1,2,2,3],
#
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
class Solution:
    def removeDuplicates(self, nums):
        i = 1
        for j in range(2,len(nums)):
            if nums[j]!=nums[i-1]:
                i = i+1
                nums[i] = nums[j]
        return i+1
s=Solution()
print(s.removeDuplicates([0,1,1,1,1,2,2,2,3,3,3,3]))
