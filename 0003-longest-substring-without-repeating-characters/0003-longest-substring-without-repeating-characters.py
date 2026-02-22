class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        map = {}
        n = len(s)
        max_len = 0
        for r in range(0,n):
            while s[r] in map:
    
                del map[s[l]]
                l+=1
            map[s[r]] = 1
            max_len = max(max_len,r-l+1)

        return max_len
        