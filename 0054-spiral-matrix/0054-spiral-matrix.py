class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        cs = 0
        ce= len(mat[0])-1
        rs =0
        re = len(mat)-1
        res = []
        while(rs>=re or ce>=cs ):
            for i in range(cs,ce+1):
                res.append(mat[rs][i])
            
            rs+=1
            for j in range(rs,re+1):
                res.append(mat[j][ce])
                
            if(rs>re or cs>=ce):
                break
            ce-=1
            for k in range(ce,cs-1,-1):
                res.append(mat[re][k])

            re-=1
            if(rs>re or cs>=ce):
                break
            for l in range(re,rs-1,-1):
               res.append(mat[l][cs])
            cs+=1
        return res