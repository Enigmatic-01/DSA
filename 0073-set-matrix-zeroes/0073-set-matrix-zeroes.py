class Solution(object):
    
    def setZeroes(self, mat):
        def turn_rows(mat,i,m):
            for j in range(m):
                    mat[i][j]=0
                
        def turn_cols(mat,j,n):
            for i in range(n):
                    mat[i][j]=0


        n = len(mat)
        m = len(mat[0])
        rows = [0]*n
        cols= [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    rows[i] = 1
                    cols[j] =1


        for i in range(n):
            if rows[i]==1:
                turn_rows(mat,i,m)
        for i in range(m):
            if cols[i]==1:
                turn_cols(mat,i,n)

        return mat