# 给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
#
# 示例 1:
#
# 输入: [1,1,2,3,3,4,4,8,8]
# 输出: 2
#
# 示例 2:
#
# 输入: [3,3,7,7,10,11,11]
# 输出: 10
class Solution:
    def singleNonDuplicate(self, nums):
        ans = nums[0]
        for i in range(1,len(nums)):
            ans ^=nums[i]
        return ans
s=Solution()
print(s.singleNonDuplicate([3,3,7,7,10,11,11]))
