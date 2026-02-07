class Solution(object):
    def minWindow(self, s, t):
        if len(t)>len(s):
            return ""
        map = {}
        cnt = 0
        min_len = float("inf")
        r = l = 0
        n = len(s)
        m = len(t)
        st = -1
        for c in t:
            if c not in map:
                map[c]=1
            else:
                map[c]+=1
        while(r<n):
            if s[r] in map:
                if(map[s[r]]>0):
                    cnt+=1
                map[s[r]]-=1
            while(cnt==m):
                if r-l+1 < min_len:
                    min_len= r-l+1
                    st = l
                if s[l] in map:
                    map[s[l]]+=1
                    if map[s[l]]>0:
                        cnt-=1
                l+=1
            r+=1
        if(st==-1):
            return ""
        return s[st:st+min_len]