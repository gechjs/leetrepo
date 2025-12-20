class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
      
        @cache
        def dp(i, t_type):
            if t_type=="sell":
                maxprofit= prices[i]
                for j in range(i+2, len(prices)):
                    maxprofit = max(maxprofit, prices[i]+dp(j, "buy"))
                return maxprofit  
            else:
                maxprofit = float("-inf")
                for j in range(i+1, len(prices)):
                    if prices[j]>prices[i]:
                        maxprofit = max(maxprofit,-1*prices[i]+dp(j, "sell"))
                maxprofit = max(maxprofit, 0)
                return maxprofit
        profit = 0
        for i in range(len(prices)-1):
            profit= max(profit, dp(i, "buy"))
        return profit
