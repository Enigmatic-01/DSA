class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                
                continue
            
            j = i+1
            k = n-1
            while(j<k):
                summation = nums[i]+nums[j]+nums[k]
                if(summation==0):
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(k>j and nums[j]==nums[j-1] ):
                        j+=1
                    k-=1
                    while(k<n and k>j and nums[k]==nums[k+1] ):
                        k-=1
                elif(summation>0):
                    k-=1
                    while(k<n and k>j and nums[k]==nums[k+1] ):
                        k-=1
                else:
                    j+=1
                    while(k>j  and  nums[j]==nums[j-1] ):
                        j+=1
        return ans       
                