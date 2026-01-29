class Solution(object):
    def maxArea(self, height):
        l_ptr = 0
        r_ptr = len(height)-1
        area = float("-inf")
        while(l_ptr<r_ptr):
            width = r_ptr - l_ptr 
            if(height[r_ptr]>height[l_ptr]):
                area  = max(area,width*height[l_ptr])
                l_ptr+=1
            else:
                area  = max(area,width*height[r_ptr])
                r_ptr-=1
        
        return area