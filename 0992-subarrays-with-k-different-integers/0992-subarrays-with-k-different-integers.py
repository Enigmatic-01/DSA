class Solution(object):
    def fu(self,nums,k):
        cnt  = 0
        l = 0
        r = 0
        n = len(nums)
        map ={}
        while(r<n):
            if nums[r] not in map:
                map[nums[r]] = 1
            else:
                map[nums[r]]+=1
            while(k<len(map)):
                map[nums[l]]-=1
                if map[nums[l]]==0:
                    del map[nums[l]]
                l+=1
            cnt += r-l+1
            r+=1
        
        return cnt
    def subarraysWithKDistinct(self, nums, k):
        return self.fu(nums,k) - self.fu(nums,k-1)
        