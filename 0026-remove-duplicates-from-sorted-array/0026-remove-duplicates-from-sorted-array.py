class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        n = len(nums)
        for j in range(n):
            if(nums[i]!=nums[j]):
                nums[i+1] = nums[j]
                i+=1
        return i+1