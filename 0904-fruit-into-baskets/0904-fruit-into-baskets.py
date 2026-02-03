class Solution(object):
    def totalFruit(self, nums):
        backet = {}
        r = 0
        l = 0
        longest = 0
        k = 2

        n = len(nums)

        while(r<n):
            if nums[r] not in backet:
                backet[nums[r]]=1
            else:
                backet[nums[r]]+=1
            while(k<len(backet) and r>l):
                backet[nums[l]]-=1
                if(backet[nums[l]]==0):
                    del backet[nums[l]]
                l+=1
            longest = max(longest,r-l+1)
            
            r+=1
        return longest