class Solution(object):
    def generate(self, n):
        def fac(n):
            ans = 1
            for i in range(1,n+1):
                ans*=i
            return ans

        j = 1
        tri = []
        for n in range(n):
            j*=n
            if j==0:
                j = 1
            l = []
            for r in range(n):
                ans = j//(fac(r)*(fac(n-r)))
                l.append(ans)
            l.append(1)
            tri.append(l)
        return tri
        