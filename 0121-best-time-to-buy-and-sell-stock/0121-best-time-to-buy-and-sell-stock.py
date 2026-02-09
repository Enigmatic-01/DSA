class Solution(object):
    def maxProfit(self, price):
        profit = 0
        min_day = price[0]

        for i in range(1,len(price)):
                cost =price[i]-min_day
                min_day = min(min_day,price[i])
                profit = max(cost,profit)
        return profit