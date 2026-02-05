class Solution(object):
    def maxScore(self,nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        l= r = n-k

        max_sum  = 0
        sum  = 0

        for _ in range(2*k):
            sum+=nums[r%n]
            if(r-l+1>k):
                sum-=nums[l%n]
                l+=1
            max_sum = max(max_sum,sum)

            r+=1
        return max_sum
        