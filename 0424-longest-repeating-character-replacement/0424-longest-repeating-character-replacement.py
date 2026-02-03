class Solution(object):
    def characterReplacement(self, s, k):
        
        r = 0
        l = 0
        cnt = 0
        char_map = {}
        longest = 0
        max_freq = 0
        while(r<len(s)):
            if s[r] not in char_map:
                char_map[s[r]] = 1
                max_freq =max(char_map[s[r]],max_freq)
            else:
                char_map[s[r]]+=1
                max_freq =max(char_map[s[r]],max_freq) 
             
            while((r-l+1)-max_freq > k  ):
                char_map[s[l]]-=1
                if(char_map[s[l]]==0):
                    del char_map[s[l]]
                l+=1
    
            if((r-l+1)-max_freq<=k):  
                longest = max(longest,r-l+1)
        
            r+=1
        return longest