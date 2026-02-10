class Solution(object):
    def nextPermutation(self, nums):
        ith = -1
        n =len(nums)
        for i in range(n-1,0,-1):
            if(nums[i-1]<nums[i]):
                ith = i-1
                break

        if ith ==-1:
            l = 0
            r = n-1
            while(l<r):
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
            return nums

        for j in range(n-1,ith,-1):
            
            if(nums[j]>nums[ith]):
                nums[j],nums[ith] = nums[ith],nums[j]
                break

        l = ith+1
        r = n-1
        while(l<r):
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return nums
