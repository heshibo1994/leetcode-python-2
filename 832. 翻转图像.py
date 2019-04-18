class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        for i in range(row):
            for j in range(col//2):
                A[i][j],A[i][col-j-1] = A[i][col-j-1],A[i][j]
        for i in range(row):
            for j in range(col):
                A[i][j] = 1-A[i][j]
        return A