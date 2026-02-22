class Solution(object):
    def subarraySum(self, nums, k):
        map = {0:1}
        n = len(nums)
        cnt = 0
        summation = 0
        for r in range(n):
            summation+=nums[r]
            remain = summation-k
            if remain in map:
                 cnt+=map[remain]
            if summation not in map :
                map[summation] = 1
            else:
                map[summation]+=1
        return cnt

