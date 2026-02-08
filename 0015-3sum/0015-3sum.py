class Solution(object):
    def threeSum(self, nums):
        d_set = set()
        ans = []
        n = len(nums)
        for i in range(n-2):
            j =i+1
            k = j+1
            while(k<n):
                if(nums[i]+nums[j]+nums[k]==0):
                    r = [nums[i],nums[j],nums[k]]
                    d_set.add(tuple(sorted(r)))
                    
                
                j+=1
                k+=1
        ans = [list(x) for x in d_set]
        return ans