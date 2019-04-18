class Solution:
    def fairCandySwap(self, A, B):
        a = sum(A)
        b = sum(B)
        d = a - (a + b) // 2
        B = set(B)
        for i in A:
            if i - d in B:
                return [i, i - d]




s =Solution()
print(s.fairCandySwap([1,1],[2,2]))