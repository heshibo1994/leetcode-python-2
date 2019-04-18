# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(height)-1
        while (left != right):
            area = min(height[left],height[right])*(right-left)
            ans = max(area, ans)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans
s =Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))