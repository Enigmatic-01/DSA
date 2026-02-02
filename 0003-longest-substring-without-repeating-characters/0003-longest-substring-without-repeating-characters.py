class Solution(object):
    def lengthOfLongestSubstring(self, s):
        map = {}
        l = 0
        longest = 0
        r = 0
        while(r<len(s)):
            while(s[r] in map):
                del map[s[l]]
                l+=1   
            
            if s[r] not in map:
                map[s[r]] = 1
                r+=1
            longest = max(longest,r-l)
                

        return longest
        