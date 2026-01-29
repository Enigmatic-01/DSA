class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Optimal Sol


        # start_b = -1
        # n = len(s)
        # for i in range(n):
        #     if(s[i]=="b"):
        #         start_b = i
        #         break
    
        # flag = True
        
        # if(start_b == -1):
        #     return flag

        # for i in range(i,n):
        #     if(s[i]=="a"):
        #         flag = False
        #         break
        
        # return flag

        cnt_a = 0
        cnt_b = 0
        n = len(s)
        for i in range(n):
            if(s[i]=="b"):
                cnt_b+=1
                cnt_a = 0
            else:
                cnt_a += 1
                cnt_b = 0  
        if(cnt_a==cnt_b):
            return False
        cnt_b_a = 0
        for i in range(n):
            if(s[i]=="b"):
                cnt_b_a+=1
        return cnt_b_a == cnt_b



        
