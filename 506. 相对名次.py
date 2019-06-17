# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
#
# (注：分数越高的选手，排名越靠前。)
#
# 示例 1:
#
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/relative-ranks
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        import copy
        ans = []
        num_old = copy.copy(nums)
        nums.sort( reverse= True)
        a = {}
        a[nums[0]] = "Gold Medal"
        a[nums[1]] = "Silver Medal"
        a[nums[2]] = "Bronze Medal"
        for i in range(3,len(nums)):
            a[nums[i]] = i+1
        for i in range(len(num_old)):
            ans.append(a[num_old[i]])
        return ans
s = Solution()
print(s.findRelativeRanks([1,4,6,4,3,2,9]))
