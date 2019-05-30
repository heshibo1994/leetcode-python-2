# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = {}
        for i in nums:
            a[i] = a.get(i,0)+1
        res = sorted(a.items(), key=lambda a: a[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans
s=Solution()
s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)