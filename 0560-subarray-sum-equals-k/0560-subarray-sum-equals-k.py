class Solution(object):
    def subarraySum(self, nums, k):
        map = {}
        cnt = 0
        summation = 0
        map[0]=1
        for n in nums:
            summation += n
            remain = summation-k
            cnt+=map.get(remain,0)
            if(summation in map):
                map[summation]+=1
            else:
                map[summation]=1
        return cnt
            

