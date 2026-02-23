class NumMatrix(object):

    def __init__(self, matrix): 
        self.mat = matrix
        n = len( self.mat)
        m = len( self.mat[0])
        for i in range(m):
            for j in range(1,n):
                self.mat[j][i]+= self.mat[j-1][i]
                

    def sumRegion(self, rs, cs, re, ce):
        summation = 0
        if cs==ce:
            if rs == re and re>=1:
                summation+=(self.mat[re][cs]-self.mat[rs-1][cs])
            elif rs == 0:
                summation+=(self.mat[re][cs] )

            else:
                summation+=(self.mat[re][cs]-self.mat[rs-1][cs] )
            
        else:
            for c in range(cs,ce+1):
                if rs == 0:
                    summation+=(self.mat[re][c] )
                else:
                    summation+=(self.mat[re][c]-self.mat[rs-1][c] )
                    
        return summation
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)