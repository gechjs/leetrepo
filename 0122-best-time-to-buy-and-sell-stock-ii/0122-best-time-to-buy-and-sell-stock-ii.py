class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        buy = prices[0]
        for i in range(1, len(prices)):
            if buy<prices[i]:
                profit+=prices[i]-buy
                buy=prices[i]
            else:
                buy=prices[i]
        return profit