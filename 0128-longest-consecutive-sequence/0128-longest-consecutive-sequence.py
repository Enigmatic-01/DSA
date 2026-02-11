class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    
        
        longest_con = 0
        to_seen = set(nums)
        for x in to_seen:
            if x-1 not in to_seen:
                curr = x
                cnt = 1
                while curr+1 in to_seen:
                    curr+=1
                    cnt+=1
                longest_con = max(cnt,longest_con)
                    
           
        return longest_con