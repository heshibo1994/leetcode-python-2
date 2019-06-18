# 给定一个二进制数组, 找到含有相同数量的
# 0
# 和
# 1
# 的最长连续子数组（的长度）。
#
#
#
# 示例
# 1:
#
# 输入: [0, 1]
# 输出: 2
# 说明: [0, 1]
# 是具有相同数量0和1的最长连续子数组。
#
# 示例
# 2:
#
# 输入: [0, 1, 0]
# 输出: 2
# 说明: [0, 1](或[1, 0])
# 是具有相同数量0和1的最长连续子数组。
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / contiguous - array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] =-1
        a = {}
        s = 0
        ans = 0
        for i in range(len(nums)):
            s = s+nums[i]
            if s == 0:
                ans = i+1
            if s not in a:
                a[s] = i
            else:
                ans = max(ans,i-a[s])
        return ans
s = Solution()
print(s.findMaxLength( [0,0,1,1,1,1]))




