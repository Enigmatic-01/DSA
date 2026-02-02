class Solution(object):
    def longestOnes(self, nums, k):
        r = 0
        l = 0
        longest = 0
        cnt = 0
        n = len(nums)

        while(r<n):
            if nums[r] == 0 : cnt+=1
            while(cnt>k):
                if nums[l]==0: cnt-=1
                l+=1
            longest = max(longest,r-l+1)
            r+=1
        return longest