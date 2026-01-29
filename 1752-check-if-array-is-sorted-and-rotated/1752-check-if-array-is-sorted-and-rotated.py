class Solution(object):
    def check(self, nums):
        # Brute Force 

        # dummy = nums[:]
        # dummy.sort()
        # length = len(nums)
        # for i in range(length):
        #     flag = True
        #     first = dummy[0]
        #     for j in range(length - 1):
        #         dummy[j] = dummy[j+1]
        #     dummy[-1] = first
        #     for k in range(length):
        #         if(nums[k]!=dummy[k]):
        #             flag = False
        #             break
        #     if(flag is True):
        #         return True
        # return False
        if(len(nums)==1):
            return True
        cnt = 1
        length = len(nums)
        for i in range((length*2)-1):
            if(nums[i%length]<=nums[(i+1)%length]):
                cnt+=1
            else:
                cnt = 1
            if(cnt==length):
                return True
        return False

        