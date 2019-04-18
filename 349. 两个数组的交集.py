class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = list(set(nums1))
        ans = []
        for i in l1:
            if i in nums2:
                ans.append(i)
        return ans
