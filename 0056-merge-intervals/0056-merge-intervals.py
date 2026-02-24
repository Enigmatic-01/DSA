class Solution(object):
    def merge(self, nums):
        nums.sort()
        res= []
        n = len(nums)
        for i in range(n):
            if len(res)==0 or res[-1][1]<nums[i][0]:
                res.append(nums[i])
            else:
                el = max(nums[i][1],res[-1][1])
                res[-1][1]=el
        return res
