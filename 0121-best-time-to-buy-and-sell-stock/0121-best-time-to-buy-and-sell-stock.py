class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_purchase = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_purchase)
            min_purchase = min(min_purchase, prices[i])
        
        return max_profit
        