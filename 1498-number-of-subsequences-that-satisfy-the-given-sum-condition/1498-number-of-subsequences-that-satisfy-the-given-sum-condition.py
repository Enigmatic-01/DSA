class Solution(object):
    def numSubseq(self, nums, target):
        cnt =0
        left = 0
        nums.sort() 
        right = len(nums) - 1
        MOD = (10**9)+7
        powers = [1]*len(nums)
        for i in range(1,len(nums)):
            powers[i] = (powers[i-1] * 2) % MOD
        while(left<=right):
            if(nums[left]+nums[right]<=target):
                cnt+=powers[right-left]
                cnt%= MOD
                left+=1
            else:
                right-=1
        return cnt
        