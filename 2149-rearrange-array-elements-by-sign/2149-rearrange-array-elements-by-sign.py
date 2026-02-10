class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res= [0]*len(nums)
        pos = 0
        neg = 1

        for n in nums:
            if(n>0):
                res[pos] = n
                pos+=2
            else:
                res[neg]=n
                neg+= 2
                

        return res