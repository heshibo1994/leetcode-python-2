# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#     所有数字都是正整数。
#     解集不能包含重复的组合。
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1,2,3,4,5,6,7,8,9]
        ans = []
        def dfs(start,l):
            if len(l) ==k and sum(l) ==n:
                ans.append(l[:])
                return
            for i in range(start,9):
                l.append(nums[i])
                dfs(i+1,l)
                l.pop()
        dfs(0,[])
        return ans
s =Solution()
print(s.combinationSum3(k = 3, n = 9))