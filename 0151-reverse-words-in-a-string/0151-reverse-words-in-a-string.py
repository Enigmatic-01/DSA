class Solution(object):
    def reverseWords(self, s):
        res = ""
        ans = ""
        for c in s:
            if(c == " "):
                if(len(ans)):
                    if(len(res)):
                        res = ans+" "+res
                    else:
                        res = ans+res
                    ans = ""
                    continue
            else:
                ans+=c
        if(len(ans) and len(res)):
            res = ans+" "+res
        elif(len(ans) and len(res)==0):
            res = ans
    
        return res