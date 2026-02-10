class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos= []
        neg = []
        for n in nums:
            if(n<0):
                neg.append(n)
            else:
                pos.append(n)
                
        n = len(pos)
        m = len(neg)

        i = 0
        j = 0

        for k in range(len(nums)):
            if(k%2==0):
                nums[k]=pos[i]
                i+=1
            else:
                nums[k]=neg[j]
                j+=1
        return nums