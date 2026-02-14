class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        elFirst = -1
        elSec = -1
        cntFirst = 0
        cntSec = 0
        for i in range(n):
            if cntFirst ==0:
                elFirst = nums[i]
                cntFirst+=1
            elif  cntSec ==0:
                elSec=nums[i]
                cntSec+=1
            elif nums[i]==elFirst :
                cntFirst+=1
            elif nums[i] == elSec:
                cntSec+=1
            else:
                cntFirst-=1
                cntSec-=1
               
        cntfirstCheck = 0
        cntsecCheck = 0
        for i in range(n):
            if nums[i]==elFirst:
                cntfirstCheck+=1
            elif nums[i] == elSec:
                cntsecCheck+=1
        ans= []
        if cntfirstCheck>n//3:
            ans.append(elFirst)
        if cntsecCheck>n//3:
            ans.append(elSec)
        return ans