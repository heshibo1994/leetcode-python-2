# 350. 两个数组的交集 II
class Solution:
    def intersect(self, nums1,nums2):
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans

s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))


