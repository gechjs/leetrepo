class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minval = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-minval)
            minval = min(minval, prices[i])
        return profit