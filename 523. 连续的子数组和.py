# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
#
# 示例 1:
#
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
#
# 示例 2:
#
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/continuous-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        lookup[0] = -1
        # print(lookup)
        summing = 0
        n = len(nums)
        if n < 2 : return False
        for i in range(0,n):
            summing += nums[i]
            if k!= 0:summing %= k
            pre = lookup.get(summing,None)
            # print(lookup)
            if pre != None:
                if i - pre > 1:
                    return True
            else:
                lookup[summing] = i
        return False

