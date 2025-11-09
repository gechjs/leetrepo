class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        ans = 0
        buy = float(inf)
        sell = 0
        for i in range(len(prices)):
            
            if buy>prices[i]:
                buy = prices[i]
                sell = 0
            elif sell>prices[i]:
                ans+=sell-buy
                sell = 0
                buy = prices[i]
            else:
                sell = max(sell, prices[i])
        if sell-buy> 0:
            ans = ans + sell-buy
        return ans

