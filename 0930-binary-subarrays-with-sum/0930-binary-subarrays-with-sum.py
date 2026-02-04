class Solution(object):
    def helper(self,nums,goal):
        if(goal<0):return 0
        r = 0
        l = 0
        n = len(nums)
        cnt = 0
        summation = 0
        while(r<n):
            summation+=nums[r]
            while(summation>goal):
                summation-=nums[l]
                l+=1
            
            cnt += r-l+1
            r+=1
        return cnt
    def numSubarraysWithSum(self, nums, goal):
        return self.helper(nums,goal)-self.helper(nums,goal-1)
        
        