class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float("-inf")
        if (len(nums)==1):
            return nums[0]
        summation = 0
        for n in nums:
            summation+=n
            max_sum = max(summation,max_sum)
            if summation<0:
                summation = 0
            

       
        
        return max_sum
            
        