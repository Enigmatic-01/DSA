class Solution(object):
    def findTheLongestSubstring(self, s):
        cnt = 0
        mark = 0
        prefix_mark = {0:-1}
        map = {"a":0,"e":0,"i":0,"o":0,"u":0}
        for i,c in enumerate(s):
            if(c in "aeiou"):
                mark^=1+(ord(c)-ord("a"))
            if(mark in prefix_mark):
                curr_len = i-prefix_mark[mark]
                cnt = max(cnt,curr_len)
            else:
                prefix_mark[mark]=i
        return cnt
        