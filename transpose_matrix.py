class Solution:
    def transpose(self, mat):
        n = len(mat)
        m = len(mat[0])
        transposed = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                transposed[j][i] = mat[i][j]
        return transposed



