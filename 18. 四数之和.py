# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        l = len(nums)
        ans = []
        for i in range(l-3):
            for j in range(i+1,l-2):
                t =target-(nums[i]+nums[j])
                start = j+1
                end = l-1
                while start<end:
                    if nums[start]+nums[end]<t:
                        start = start+1
                    elif nums[start]+nums[end]>t:
                        end =end-1
                    else:
                        if [nums[i],nums[j],nums[start],nums[end]] not in ans:
                            ans.append([nums[i],nums[j],nums[start],nums[end]])
                        start = start+1
                        end = end-1
        return ans
s=Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))



