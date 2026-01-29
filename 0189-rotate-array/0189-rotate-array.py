class Solution(object):
    def rotate(self, nums, k):
        if(len(nums)==1 or k==0 or k==len(nums)):
            return nums
        
        # n = len(nums)
        # dummy = nums[:]
        # for i in range(k):
        #     first = dummy[-1]
        #     for j in range(n-1,0,-1):
        #         dummy[j] = dummy[j-1]
        #     dummy[0] = first
        # for i in range(n):
        #     nums[i] = dummy[i]
        # return nums
        n = len(nums)
        k = k%n
        def rev(nums,l,r):
            left = l
            right = r
            while(left<=right):
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        rev(nums,n-k,n-1)
        rev(nums, 0, n - k - 1)
        rev(nums,0,n-1)
        return  nums
