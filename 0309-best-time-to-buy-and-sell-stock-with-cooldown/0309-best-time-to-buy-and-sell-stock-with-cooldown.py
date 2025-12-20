class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dp(i, t_type):
            if (i, t_type) in memo:
                return memo[(i, t_type)]
            if i==len(prices)-1:
                if t_type=="sell":
                    return prices[i]
                else:
                    return 0
                
            if t_type=="sell":
                maxprofit= prices[i]
                for j in range(i+2, len(prices)):
                    maxprofit = max(maxprofit, prices[i]+dp(j, "buy"))
                memo[(i, t_type)]=maxprofit
                return memo[(i, t_type)]
            else:
                maxprofit = float("-inf")
                for j in range(i+1, len(prices)):
                    maxprofit = max(maxprofit,-1*prices[i]+dp(j, "sell"))
                memo[(i, t_type)]=maxprofit
                return memo[(i, t_type)]
        profit = 0
        for i in range(len(prices)):
            profit= max(profit, dp(i, "buy"))
        return profit
