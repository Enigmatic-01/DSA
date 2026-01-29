class Solution(object):
    def numRescueBoats(self, people, limit):
        cnt = 0 
        right= len(people)-1
        left = 0
        people.sort()
        while(left<=right):
            if(people[left]+people[right]<=limit):
                left+=1
                right-=1
            else:
                right -=1
            cnt+=1 

        return cnt
