class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        map = {}
        n = len(nums)
        max_len = 0
        summation = 0
        for r in range(0,n):
            summation+=nums[r]
            while k<(r-l+1 - summation):
                summation-=nums[l]
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len