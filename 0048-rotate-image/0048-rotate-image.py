class Solution(object):
    def rotate(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(i,n):
                if i!=j:
                    mat[j][i],mat[i][j] = mat[i][j],mat[j][i]

        for i in range(n):
            mat[i].reverse()
        return mat
        