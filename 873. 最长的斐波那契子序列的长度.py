# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
#
#     n >= 3
#     对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
#
# 给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
#
# （回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
class Solution:
    def lenLongestFibSubseq(self, A):
        left = 0
        right =1
        ans = []
        while right<len(S):
            if S[left] == S[right]:
                right += 1
            else:
                if right - left>2:
                    ans.append([left,right-1])
                left = right
                right = left+1
        if right - left > 2:
            ans.append([left, right - 1])
        return ans


