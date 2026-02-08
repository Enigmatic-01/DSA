class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)
        nums.sort()


        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k = n-1
                l = j+1
                while(l<k):
                    summation = nums[i]+nums[j]+nums[k]+nums[l]
                    
                    if(summation==target):
                        ans.append([nums[i],nums[j],nums[l],nums[k]])
                        l+=1
                        while(k>l and nums[l]==nums[l-1] ):
                            l+=1
                        k-=1
                        while(k<n and k>l and nums[k]==nums[k+1] ):
                            k-=1
                    elif(summation>target):
                        k-=1
                        while(k<n and k>l and nums[k]==nums[k+1] ):
                            k-=1
                    else:
                        l+=1
                        while(k>l  and  nums[l]==nums[l-1] ):
                            l+=1
        return ans