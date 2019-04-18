# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。



class Solution:
    def longestConsecutive(self, nums):
        nums=list(set(nums))
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        ans = 0
        temp = [nums[0]]
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp.append(nums[i + 1])
            else:
                ans = max(ans,len(temp))
                temp = [nums[i + 1]]
        if nums[-1] - nums[-2] == 1:
            ans = max(ans,len(temp))
        return ans
s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
