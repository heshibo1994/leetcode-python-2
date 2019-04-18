# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: 210
#
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=lambda a:str(a)[0],reverse=True)
        ans = ""
        temp = []
        for i in range(len(nums)):
            for j in range(9,-1,-1):
                if str(nums[i])[0] == j:
                    temp.append(nums[i])


        def dfs(start,l):
            pass



        return nums
s = Solution()
print(s.largestNumber([3,30,34,5,2,9]))